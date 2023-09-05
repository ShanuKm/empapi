from django.db import models
# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    department=models.CharField(max_length=10)
