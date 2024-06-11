from django import forms
from django.core.exceptions import ValidationError

from .models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_confrim_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Password DON'T MATCH")
        
        return password
    

class UserLogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'