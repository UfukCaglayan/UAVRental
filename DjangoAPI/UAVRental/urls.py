from django.contrib import admin
from django.urls import path
from UAVRental import views #add myapp
 
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('signup/',views.signup),
    path('profile/',views.profile),
    path('rental/<int:id>', views.rental,name="rental"),

]