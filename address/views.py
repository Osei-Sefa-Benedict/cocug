from django.shortcuts import render, redirect
from .models import District, Region, Ministry
from .forms import DistrictForm, RegionForm, MinistryForm

def load_Region(request):
    district_id = request.GET.get('district')
    print('....................')
    print(district_id)
    Region = Region.objects.filter(district_id=district_id).order_by('name')
    context = {
        'Region': Region
    }
    return render(request, 'administration/Region_dropdown_list_options.html', context)

def load_Ministry(request):
    Region_id = request.GET.get('Region')
    Ministry = Ministry.objects.filter(Region_id=Region_id).order_by('name')
    context = {
        'Ministry': Ministry
    }
    return render(request, 'others/Ministry_dropdown_list_options.html', context)


def add_district(request):
    forms = DistrictForm()
    if request.method == 'POST':
        forms = DistrictForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('district')
    district = District.objects.all()
    context = {'forms': forms, 'district': district}
    return render(request, 'address/district.html', context)

def add_Region(request):
    forms = RegionForm()
    if request.method == 'POST':
        forms = RegionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Region')
    Region = Region.objects.all()
    context = {'forms': forms, 'Region': Region}
    return render(request, 'address/Region.html', context)

def add_Ministry(request):
    forms = MinistryForm()
    if request.method == 'POST':
        forms = MinistryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Ministry')
    Ministry = Ministry.objects.all()
    context = {'forms': forms, 'Ministry': Ministry}
    return render(request, 'address/Ministry.html', context)

