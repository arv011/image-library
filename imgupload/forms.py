from django import forms
from .models import Pic

class imgform(forms.ModelForm):
    class Meta:
        model = Pic
        fields = ('image', 'description')
        labels = {'image':''}