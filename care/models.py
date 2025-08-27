from django.db import models

# Create your models here.
class Doctor(models.Model):
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=15)

class Patient(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE)
    phone = models.CharField(max_length=10)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=7)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    STATUS_SCHEDULE = 'S'
    STATUS_COMPLETED = 'C'
    STATUS_CANCELLED = 'P'

    STATUS_CHOICES = [
        (STATUS_SCHEDULE, 'Scheduled'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    appointment_date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default=STATUS_SCHEDULE)

class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='treatments')
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    medication = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)