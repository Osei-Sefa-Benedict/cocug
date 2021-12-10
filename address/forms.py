from django import forms
from .models import District, Region, Ministry


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        widgets = {
            'district': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = '__all__'
        widgets = {
            'district': forms.Select(attrs={'class': 'form-control'}),
            'Region': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
