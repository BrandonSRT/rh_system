from operator import mod
from django.db import models



class Country(models.Model):
    country_name = models.CharField(max_length=25)


class Jobs(models.Model):
    job_name = models.CharField(max_length=25)




class Candidate (models.Model):
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    identification = models.CharField(max_length=40)
    nationality = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    direction = models.CharField(max_length=250)
    birth_date = models.DateTimeField(max_length=40)
    candidate_phone = models.CharField(max_length=40)
    mail = models.EmailField(max_length=40)
    civil_status = models.CharField(max_length=40)
    spouse = models.CharField(max_length=40)
    children_option = models.BooleanField(max_length=40)
    children_quantity = models.CharField(max_length=40)
    dependency_quantity = models.CharField(max_length=40)
    blood_type = models.CharField(max_length=40)
    license_type = models.CharField(max_length=40)
    vehicle_option = models.BooleanField(max_length=40)
    profession = models.CharField(max_length=40)
    job = models.ForeignKey(Jobs, null=True, on_delete=models.SET_NULL)
    salary = models.CharField(max_length=40)
    date = models.DateTimeField(max_length=40)
    studies = models.CharField(max_length=40)
    illness_option = models.BooleanField(max_length=40)
    illness = models.CharField(max_length=40)
    company_name = models.CharField(max_length=40)
    compnay_phone = models.CharField(max_length=40)
    old_job = models.CharField(max_length=40)
    final_salary = models.CharField(max_length=40)
    entry_date = models.DateTimeField(max_length=40)
    departure_date = models.DateTimeField(max_length=40)
    boss_name = models.CharField(max_length=40)
    exit_reason = models.CharField(max_length=40)
    family_option = models.BooleanField(max_length=40)
    familiar = models.CharField(max_length=40)
    photo = models.ImageField()
    cv = models.FileField()
    handling_option = models.BooleanField(max_length=40)
    other_studies = models.CharField(max_length=250)
    profesional_code= models.CharField(max_length=50)
    person_name1 = models.CharField(max_length=40)
    person_phone1 = models.CharField(max_length=40)
    person_name2 = models.CharField(max_length=40)
    person_phone2 = models.CharField(max_length=40)
    vehicle_description = models.CharField(max_length=40)
    hogar_employee = models.CharField(max_length=250, null=True, blank=True)

class HR_Form (models.Model):
    ref_num = models.IntegerField()
    name = models.CharField(max_length=40)
    interviewed = models.BooleanField(max_length=40, null=True, blank=True)
    result1 = models.BooleanField(max_length=40, null=True, blank=True)
    observaciones1 = models.CharField(max_length=250, null=True, blank=True)
    terapy = models.BooleanField(max_length=40, null=True, blank=True)
    result2 = models.BooleanField(max_length=40, null=True, blank=True)
    observaciones2 = models.CharField(max_length=250, null=True, blank=True)
    medicalval = models.BooleanField(max_length=40, null=True, blank=True)
    result3 = models.BooleanField(max_length=40, null=True, blank=True)
    observaciones3 = models.CharField(max_length=250, null=True, blank=True)
    psychometric = models.BooleanField(max_length=40, null=True, blank=True)
    result4 = models.CharField(max_length=250, null=True, blank=True)
    observaciones4 = models.CharField(max_length=250, null=True, blank=True)
    interview_date = models.DateTimeField(max_length=40)
    interviewers = models.CharField(max_length=250, null=True, blank=True)
    test_file = models.FileField(null=True, blank=True)


