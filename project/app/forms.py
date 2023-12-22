from django import forms
from .models import *


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
