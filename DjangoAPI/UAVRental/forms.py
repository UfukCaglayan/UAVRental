from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Resim ekleme işleminin yapılabilmesini sağlayan form
class UploadForm(forms.Form):
    image = forms.ImageField()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
