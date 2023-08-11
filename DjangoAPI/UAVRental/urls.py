from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from UAVRental import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('signup/',views.signup),
    path('profile/',views.profile),
    path('rental/<int:id>', views.rental,name="rental"),
    url('myrental/',views.myrental,name='myrental'),
    url(r'^create$', views.create, name='create'),
    url('rental/create$', views.create, name='create'),
    url(r'^rental/create/$', views.create, name='create'),

     url('myrental/', views.myrental, name='myrental'),
    url(r'^myrental', views.myrental, name='myrental'),
]