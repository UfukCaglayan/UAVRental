from django import forms

#Resim ekleme işleminin yapılabilmesini sağlayan form
class UploadForm(forms.Form):
    image = forms.ImageField()

   
