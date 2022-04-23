from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups'