import datetime
from django.contrib.auth.models import User
from django  import forms
from django.utils.html import format_html

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class UserLoginForm(AuthenticationForm):
    # Customize fields if needed
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm):
    # Customize fields if needed
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']