from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['name', 'email', 'course', 'semester', 'password']

        widgets = { 
           'name': forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}), 
           'email': forms.EmailField(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}), 
           'course': forms.CharField(attrs={'class': 'form-select'}), 
           'semester': forms.IntegerField(attrs={'class': 'form-select'}), 
           'password': forms.CharField(attrs={'class': 'form-control'}), 
       }
        