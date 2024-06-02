# forms.py
from django import forms
from .models import RegisterData

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterData
        fields = ['username', 'email', 'role', 'country', 'nationality', 'mobile', 'password']
