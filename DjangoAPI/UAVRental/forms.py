from django import forms
from django.forms import SelectMultiple, TextInput, Textarea

from UAVRental.models import Rental

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ('UavID','CustomerID','BeginDate','EndDate','Created')

   