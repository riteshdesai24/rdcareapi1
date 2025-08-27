from django.db import models
from care.models import Doctor

# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    pincode = models.CharField(max_length=7)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)