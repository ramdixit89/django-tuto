
from django import forms
from .models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User

        fields = ['name', 'email', 'course', 'semester', 'password']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'course': forms.Select(attrs={
                'class': 'form-select'
            }),

            'semester': forms.Select(attrs={
                'class': 'form-select'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
        }
