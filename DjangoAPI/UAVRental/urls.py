from django.contrib import admin
from django.urls import path, include
from UAVRental import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('rental/<int:id>/', views.rental, name="rental"),
    path('myrental/<int:id>/', views.my_rental, name='my_rental'),
    path('rentaledit/<int:id>/', views.edit_rental, name="edit_rental"),
    path('confirmDelete/<int:id>/', views.confirm_delete, name="confirm_delete"),
    path('rental/createRental/', views.create_rental, name='create_rental'),
    path('rentaledit/updateRental/', views.update_rental, name='update_rental'),
    path('confirmDelete/deleteRental/', views.delete_rental, name='delete_rental'),
]

# Sayfalar arası yönlendirme işlemlerinin yapılabilmesi için gerekli kodlar yazılmıştır. 
# Views içinde bulunan ve sayfalar için kullanılan metodlar aktif hale getirilmektedir.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Resme tıklandığında açılması için gerekli maskeleme işlemi yapılmıştır.
