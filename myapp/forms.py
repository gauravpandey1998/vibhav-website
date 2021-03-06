from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import UserProfile
from django.db import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=(
            'name',
            'phone',
        )