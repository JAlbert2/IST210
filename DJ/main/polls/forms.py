from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ("user", 'creation', 'age', 'covid')