from django import forms
from .models import RegisterModel

# Form Class
class RegisterForm(forms.ModelForm):
    confirm = forms.CharField(
        max_length=255
    )

    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm']