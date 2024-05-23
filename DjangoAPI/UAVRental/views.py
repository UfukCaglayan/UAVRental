from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Uav, Rental, Brand, Model, Category
from .forms import CustomUserCreationForm
from django.utils import timezone
from .tasks import send_email_task
from datetime import datetime

# Site ilk açıldığında mevcut İHA'ların listelenmesi
def index(request):
    uav_list = Uav.objects.order_by('uav_id')
    brand_list = Brand.objects.order_by('brand_id')
    model_list = Model.objects.order_by('model_id')
    category_list = Category.objects.order_by('category_id')
    brand_ids = []
    model_ids = []
    category_ids = []

    if request.method == "POST":
        brand_ids = request.POST.getlist('cbBrand')
        model_ids = request.POST.getlist('cbModel')
        category_ids = request.POST.getlist('cbCategory')

        if not brand_ids and not model_ids and not category_ids:
            uav_list = Uav.objects.order_by('uav_id')
        else:
            uav_list = Uav.objects.filter(brand_id__in=brand_ids) | Uav.objects.filter(model_id__in=model_ids) | Uav.objects.filter(category_id__in=category_ids)

    context = {
        'uav_list': uav_list,
        'brand_list': brand_list,
        'model_list': model_list,
        'category_list': category_list,
    }

    return render(request, 'index.html', context)

# Formdan alınan bilgilerle kayıt işleminin yapılması
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})

# Giriş işleminin yapılması
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

# Çıkış işleminin yapılması
def signout(request):
    logout(request)
    return redirect('/')

# Anasayfada kiralama butonuna tıklanmasıyla beraber kiralama işleminin yapılacağı sayfada İHA bilgilerinin görüntülenmesi
def rental(request, id):
    uav = get_object_or_404(Uav, pk=id)
    context = {'uav': uav}
    return render(request, 'rental.html', context)

# Formdan İHA, müşteri ve tarih-zaman bilgilerinin alınmasıyla beraber kiralama işlemi yapılmaktadır ve mevcut kiralama
# bilgilerinin listelendiği sayfaya yönlendirme işlemi yapılmıştır.
def create_rental(request):
    if request.method == 'POST':
        # datetime stringlerini datetime objelerine dönüştürme
        begin_date = datetime.strptime(request.POST['begin_date'], '%Y-%m-%dT%H:%M')
        end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%dT%H:%M')

        # datetime objelerini timezone-aware yapma
        begin_date = timezone.make_aware(begin_date, timezone.get_current_timezone())
        end_date = timezone.make_aware(end_date, timezone.get_current_timezone())

        rental = Rental(
            uav=Uav.objects.get(uav_id=request.POST['uav_id']),
            customer_id=request.POST['customer_id'],
            begin_date=begin_date,
            end_date=end_date
        )
        rental.save()
        
        save_to_excel(rental, request)
        send_email_task.delay('Kiralama Onayı', 'Kiralama işleminiz başarıyla tamamlanmıştır', [request.user.email])  # kullanıcıya mail gönderme işlemi kuyruğa alınmıştır
    return redirect('/myrental/' + request.POST['customer_id'])

def save_to_excel(rental, request):
    username = request.user.username
    uav = get_object_or_404(Uav, pk=rental.uav.uav_id)
    brand_model = uav.brand.brand_name + ' ' + uav.model.model_name
    begin_date = rental.begin_date.strftime("%Y-%m-%dT%H:%M:%S")
    end_date = rental.end_date.strftime("%Y-%m-%dT%H:%M:%S")
    save_to_excel.delay(username, brand_model, begin_date, end_date)  # raporlama işlemi kuyruğa alınmıştır

# Kiralama kayıtlarının gösterilmesi
@csrf_exempt
def my_rental(request, id):
    rentals = Rental.objects.filter(customer_id=id)
    context = {'rentals': rentals}
    return render(request, 'myrental.html', context)

# Listenen tıklanan kiralama kaydının düzenleme sayfasında doldurulması.
# Bu işlem sırasında tarih ve saat bilgileri inputların algılayabileceği şekilde formatlanmıştır.
def edit_rental(request, id):
    rental = get_object_or_404(Rental, pk=id)
    begin_date = rental.begin_date.strftime("%Y-%m-%dT%H:%M:%S")
    rental.begin_date = begin_date
    end_date = rental.end_date.strftime("%Y-%m-%dT%H:%M:%S")
    rental.end_date = end_date
    context = {
        'rental': rental
    }
    return render(request, 'rentaledit.html', context)

# Tarih ve saat bilgilerinin değiştirilmesiyle beraber kiralama kaydının güncellenmesi
@csrf_exempt
def update_rental(request):
    rental = get_object_or_404(Rental, pk=request.POST['rental_id'])
    rental.begin_date = request.POST['begin_date']
    rental.end_date = request.POST['end_date']
    rental.save()
    return redirect('/myrental/' + request.POST['customer_id'])

# Kiralama kaydının silinmesinin sorulması
@csrf_exempt
def confirm_delete(request, id):
    rental = get_object_or_404(Rental, pk=id)
    context = {'rental': rental}
    return render(request, 'confirm_delete.html', context)

# Kiralama kaydının silinmesi
@csrf_exempt
def delete_rental(request):
    rental = get_object_or_404(Rental, pk=request.POST['rental_id'])
    rental.delete()
    return redirect('/myrental/' + request.POST['customer_id'])

# Admin kullanıcı kontrolü
def is_admin(user):
    return user.is_superuser
