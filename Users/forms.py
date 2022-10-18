from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Users.models import *

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserCreationForm):
  class Meta:
    model = User
    fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarForm(forms.ModelForm):
  class Meta:
    model = Avatar
    fields = ["imagen"]