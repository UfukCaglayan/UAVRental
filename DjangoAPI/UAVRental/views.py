from django.http import HttpResponse
from django.template import loader
 
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from .models import Uavs,Rental
from django.views.decorators.csrf import csrf_exempt
 
def index(request):
    uav_list = Uavs.objects.order_by('UavID')
    context = {'uav_list': uav_list}
    return render(request, 'index.html', context)

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
  
def home(request): 
    return render(request, 'home.html')
  
 
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
 
def profile(request): 
    return render(request, 'profile.html')
  
def signout(request):
    logout(request)
    return redirect('/')

def rental(request, id):
    uav = get_object_or_404(Uavs, pk=id)
    context = {
        'uav': uav
    }
    return render(request, 'rental.html', context)

@csrf_exempt
def create(request):
    rental = Rental(UavID=request.POST['UavID'],CustomerID=request.POST['CustomerID'],BeginDate=request.POST['BeginDate'], EndDate=request.POST['EndDate'])
    rental.save()
    return redirect('/myrental.html')
@csrf_exempt
def myrental(request):
    rentals = Rental.objects.all()
    context = {'rentals': rentals}
    return render(request, 'myrental.html', context)

def isAdmin(user):
    return user.is_superuser


