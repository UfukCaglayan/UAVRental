from django.contrib import admin
from django.urls import path, include
from UAVRental import views
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('signup/', views.signup),
    path('profile/', views.profile),
    path('rental/<int:id>/', views.rental, name="rental"),
    path('myrental/<int:id>/', views.myrental, name='myrental'),
    path('rentaledit/<int:id>/', views.editRental, name="editRental"),
    path('confirmDelete/<int:id>/', views.confirmDelete, name="confirmDelete"),
    path('rental/createRental/', views.createRental, name='createRental'),  # Güncellendi
    path('rentaledit/updateRental/', views.updateRental, name='updateRental'),
    path('confirmDelete/deleteRental/', views.deleteRental, name='deleteRental'),
]

# Sayfalar arası yönlendirme işlemlerinin yapılabilmesi için gerekli kodlar yazılmıştır. 
# Viewsin içinde bulunan ve sayfalar için kullanılan metodlar aktif hale getirilmektedir.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Resme tıklandığında açılması için gerekli maskeleme işlemi yapılmıştır.
