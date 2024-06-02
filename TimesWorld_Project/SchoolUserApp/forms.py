from django import forms

from SchoolUserApp.models import RegisterData


from django import forms
from .models import RegisterData

class RegisterDataForm(forms.ModelForm):
    class Meta:
        model = RegisterData
        fields = ['username', 'email', 'role', 'country', 'nationality', 'mobile', 'password']
