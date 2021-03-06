from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import request


def validate_passwords(password,password2):
    special_characters = "[~!@#$%^&*()\+{}\":;'\[\]]"
    if len(password) <8 :
        raise ValidationError('Password must be at least 8 characters long.')
    if password!=password2:
        raise ValidationError("Password need to match")
    if not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least 1 digit.')
    if not any(char.islower() for char in password):
        raise ValidationError('Password must contain at least 1 lowercase letter.')
    if not any(char.isupper() for char in password):
        raise ValidationError('Password must contain at least 1 uppercase letter.')
    if not any(char in special_characters for char in password):
        raise ValidationError('Password must contain at least 1 special letter from '+ special_characters)


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')
        widgets = {
            "password": forms.PasswordInput,
        }

class ChangePasswordForm(forms.Form):
    wprowadz_haslo=forms.CharField(max_length=30, widget=forms.PasswordInput)
    powtorz_haslo=forms.CharField(max_length=30, widget=forms.PasswordInput)

class LinkToChangePasswordForm(forms.Form):
    email = forms.EmailField(required=True)


