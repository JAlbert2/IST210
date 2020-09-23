from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("user", 'age', 'creation', 'covid')