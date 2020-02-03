from django.db import models


# from django.contrib.auth.models import User

# Create your models here.
class EmpData(models.Model):  # database name is EmpData,for storing Employee details

    Emp_name = models.CharField(max_length=100)
    Emp_email = models.EmailField(max_length=50)
    Emp_phonNO = models.IntegerField(default=00)
    Emp_dept = models.CharField(max_length=25, default="NA")


class studentData(models.Model):  # database name is EmpData,for storing Employee details
    stud_name = models.CharField(max_length=100)
    stud_last = models.CharField(max_length=50)
    stud_country = models.CharField(max_length=10)
    stud_subject = models.CharField(max_length=200, default="NA")