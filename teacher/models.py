from django.db import models
from academic.models import Department
from administration.models import Designation
from address.models import District, Region, Ministry


class AddressInfo(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    Region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    Ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, null=True)
    Town = models.TextField()

    def __str__(self):
        return self.Town

class EducationInfo(models.Model):
    name_of_exam = models.CharField(max_length=100)
    institute = models.CharField(max_length=255)
    group = models.CharField(max_length=100)
    grade = models.CharField(max_length=45)
    Position = models.CharField(max_length=45)
    passing_year = models.IntegerField()

    def __str__(self):
        return self.name_of_exam

class TrainingInfo(models.Model):
    training_name = models.CharField(max_length=100)
    year = models.IntegerField()
    duration = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.training_name

class JobInfo(models.Model):
    category_choice = (
        ('bcs', 'BCS'),
        ('nationalized', 'Nationalized'),
        ('10% quota', '10% quota'),
        ('non govt.', 'Non Govt.')
    )
    category = models.CharField(choices=category_choice, max_length=45)
    joning_date = models.DateField()
    institute_name = models.CharField(max_length=100)
    job_designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    scale = models.IntegerField()
    grade_of_post = models.CharField(max_length=45)
    Year_Into_The_University = models.IntegerField()
    Year_Of_Graduation = models.IntegerField()
    promotion_due_year = models.IntegerField()
    recreation_leave_due_year = models.IntegerField()
    expected_retirement_year = models.IntegerField()

    def __str__(self):
        return self.institute_name

class ExperienceInfo(models.Model):
    institute_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=45)
    trainer = models.CharField(max_length=45)

    def __str__(self):
        return self.institute_name

class PersonalInfo(models.Model):
    name = models.CharField(max_length=45)
    photo = models.ImageField()
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=45)
    Hall_choice = (
        ('Bangladeshi', 'Bangladeshi'),
        ('Others', 'Others')
    )
    Hall = models.CharField(max_length=45, choices=Hall_choice)
    Program_choice = (
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Others', 'Others')
    )
    Program = models.CharField(max_length=45, choices=Program_choice)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = models.CharField(choices=blood_group_choice, max_length=5)
    level = models.IntegerField(unique=True)
    nid = models.IntegerField(unique=True)
    #driving_license_passport = models.IntegerField(unique=True)
    phone_no = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=255, unique=True)
    Parent_Name = models.CharField(max_length=45)
    Name_Of_Mother_Church = models.CharField(max_length=45)
    Scholarship_Beneficiary_choice = (
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single')
    )
    Scholarship_Beneficiary = models.CharField(choices=Scholarship_Beneficiary_choice, max_length=10)
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE, null=True)
    education = models.ForeignKey(EducationInfo, on_delete=models.CASCADE, null=True)
    training = models.ForeignKey(TrainingInfo, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    experience = models.ForeignKey(ExperienceInfo, on_delete=models.CASCADE, null=True)
    is_delete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
