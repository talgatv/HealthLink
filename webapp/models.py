from django.db import models


class Client(models.Model):
    name.CharField
    last_name.CharField
    given_name.CharField
    record_number
    insurance_number.CharField
    phone.CharField
    adress.CharField

class Record(models.Model):
    date.DateField
    client_id.CharField
    complains.TextField
    life_and_medical_history.TextField
    physical_exam_results.TextField
    diagnosis.TextField
    test_result.TextField
    differential_diagnosis.TextField
    

class Personnel(models.Model):
    name.CharField
    last_name.CharField
    given_name.CharField
    speciality forgen key speciality
    hospital
class Scpeciality(models.Model):
    surgery.CharField
    general_practitioner.CharField
    nurse.CharField
    other.CharField


# Create your models here.
