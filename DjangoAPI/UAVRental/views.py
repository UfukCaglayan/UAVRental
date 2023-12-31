from django.http import HttpResponse
from django.template import loader
 
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Uav,Rental,Brand,Model,Category
from django.views.decorators.csrf import csrf_exempt
from django.forms import formset_factory
from .forms import *
#Site ilk açıldığında mevcut ihaların listelenmesi
def index(request):
    uav_list = Uav.objects.order_by('UavID') 
    brand_list = Brand.objects.order_by('BrandID') #Filtreleme işlemleri için gerekli listeler dolduruluyor
    model_list = Model.objects.order_by('ModelID')
    category_list = Category.objects.order_by('CategoryID')
    brand_ids = []
    model_ids = []
    category_ids = []
    if request.method=="POST": 
        brand_ids = request.POST.getlist('cbBrand') #Tıklanan markaların value (id) listesi alınıyor
        model_ids = request.POST.getlist('cbModel')
        category_ids = request.POST.getlist('cbCategory')
        if len(brand_ids) == 0 and len(model_ids) == 0 and len(category_ids) == 0: #Hiçbir seçim yapılmadan filtreleme yapılırsa bütün İHA'lar getiriliyor 
            uav_list = Uav.objects.order_by('UavID') 
        else:
            uav_list = Uav.objects.filter(BrandID__in = brand_ids) | Uav.objects.filter(ModelID__in = model_ids) | Uav.objects.filter(CategoryID__in = category_ids)
                        #Filtreleme yapılarak id'si, tıklanan markaların id'si olan İHA'lar getiriliyor. Bu işlem model ve kategori içinde yapılıyor.
      
    context = {
        'uav_list': uav_list,
        'brand_list': brand_list,
        'model_list': model_list,
        'category_list': category_list,
    }
    return render(request, 'index.html', context)

  


#Formdan alınan bilgilerle kayıt işleminin yapılması
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    

#Giriş işleminin yapılması
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
  
#Çıkış işleminin yapılması
def signout(request):
    logout(request)
    return redirect('/')

#Anasayfada kiralama butonuna tıklanmasıyla beraber kiralama işleminin yapılacağı sayfada İHA bilgilerinin görüntülenmesi
def rental(request, id):
    uav = get_object_or_404(Uav, pk=id)
    context = {'uav': uav}
    return render(request, 'rental.html', context)

#Formdan İHA,müşteri ve tarih-zaman bilgilerinin alınmasıyla beraber kiralama işlemi yapılmaktadır ve mevcut kiralama
#bilgilerinin listelendiği sayfaya yönlendirme işlemi yapılmıştır.
@csrf_exempt
def createRental(request):
    rental = Rental(UavID= Uav.objects.get(UavID =  request.POST['UavID']) ,CustomerID=request.POST['CustomerID'],BeginDate=request.POST['BeginDate'], EndDate=request.POST['EndDate'])
    rental.save()
    return redirect('/myrental/' + request.POST['CustomerID'])

#Kiralama kayıtlarının gösterilmesi
@csrf_exempt
def myrental(request, id):
    rentals = Rental.objects.filter(CustomerID=id)
    context = {'rentals': rentals}
    return render(request, 'myrental.html', context)

#Listenen tıklanan kiralama kaydının düzenleme sayfasında doldurulması.
#Bu işlem sırasında tarih ve saat bilgileri inputların algılayabileceği şekilde formatlanmıştır.
def editRental(request, id):
    rental = get_object_or_404(Rental, pk=id)
    beginDate = rental.BeginDate.strftime("%Y-%m-%dT%H:%M:%S")
    rental.BeginDate = beginDate 
    endDate = rental.EndDate.strftime("%Y-%m-%dT%H:%M:%S")
    rental.EndDate = endDate 
    context = {
        'rental': rental
    }
    return render(request, 'rentaledit.html', context)

#Tarih ve saat bilgilerinin değiştirilmesiyle beraber kiralama kaydının güncellenmesiç
@csrf_exempt
def updateRental(request):
    rental = get_object_or_404(Rental, pk=request.POST['RentalID'])
    rental.BeginDate = request.POST['BeginDate']
    rental.EndDate = request.POST['EndDate']
    rental.save()
    return redirect('/myrental/' + request.POST['CustomerID'])

#Kiralama kaydının silinmesinin sorulması
@csrf_exempt
def confirmDelete(request, id):
    rental = get_object_or_404(Rental, pk=id)
    context = {'rental': rental}
    return render(request, 'confirmDelete.html', context)

#Kiralama kaydının silinmesi
@csrf_exempt
def deleteRental(request):
    rental = get_object_or_404(Rental, pk=request.POST['RentalID'])
    rental.delete()  
    return redirect('/myrental/' + request.POST['CustomerID'])


#Admin kullanıcı kontrolü
def isAdmin(user):
    return user.is_superuser
