from django import forms
from . import models
from academic.models import Department

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = models.PersonalInfo
        exclude = {'address', 'education', 'training', 'job', 'experience', }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'Hall': forms.TextInput(attrs={'class': 'form-control'}),
            'Program': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'nid': forms.NumberInput(attrs={'class': 'form-control'}),
            #'driving_license_passport': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Parent_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Name_Of_Mother_Church': forms.TextInput(attrs={'class': 'form-control'}),
            'Scholarship_Beneficiary': forms.Select(attrs={'class': 'form-control'}),

        }

class AddressInfoForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeAddressInfo
        fields = ('district', 'Region', 'Ministry', 'Town')
        widgets = {
            'district': forms.Select(attrs={'class': 'form-control'}),
            'Region': forms.Select(attrs={'class': 'form-control'}),
            'Ministry': forms.Select(attrs={'class': 'form-control'}),
            'Town': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Region'].queryset = models.Region.objects.none()

            if 'Region' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['Region'].queryset = models.Region.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['Region'].queryset = self.instance.district.Region_set.order_by('name')

            self.fields['Ministry'].queryset = models.Ministry.objects.none()

            if 'Ministry' in self.data:
                try:
                    Region_id = int(self.data.get('Region'))
                    self.fields['Ministry'].queryset = models.Ministry.objects.filter(Region_id=Region_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['Ministry'].queryset = self.instance.Region.Ministry_set.order_by('name')



class EducationInfoForm(forms.ModelForm):
    class Meta:
        model = models.EducationInfo
        fields = '__all__'
        widgets = {
            'name_of_exam': forms.TextInput(attrs={'class': 'form-control'}),
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
            'Position': forms.TextInput(attrs={'class': 'form-control'}),
            'passing_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TrainingInfoForm(forms.ModelForm):
    class Meta:
        model = models.TrainingInfo
        fields = '__all__'
        widgets = {
            'training_name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
        }

class JobInfoForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeJobInfo
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'joning_date': forms.TextInput(attrs={'class': 'form-control'}),
            'institute_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_designation': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'scale': forms.NumberInput(attrs={'class': 'form-control'}),
            'grade_of_post': forms.TextInput(attrs={'class': 'form-control'}),
            'Year_Into_The_University': forms.NumberInput(attrs={'class': 'form-control'}),
            'Year_Of_Graduation': forms.NumberInput(attrs={'class': 'form-control'}),
            'promotion_due_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'recreation_leave_due_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'expected_retirement_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ExperienceInfoForm(forms.ModelForm):
    class Meta:
        model = models.ExperienceInfo
        fields = '__all__'
        widgets = {
            'institute_name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'trainer': forms.TextInput(attrs={'class': 'form-control'}),
        }
