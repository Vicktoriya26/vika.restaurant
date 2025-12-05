from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Форма реєстрації
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "address", "password1", "password2")


# Форма редагування профілю
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']


