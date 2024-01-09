from django.db import models
from django import forms

from .models import Owner
class OwnerForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = '__all__'