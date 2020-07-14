from django.db import models

# Create your models here.


class SchclassModel(models.Model):
    name=models.CharField(max_length=49)
    faculty=models.CharField(max_length=49)
    date = models.DateField()
    time =models.TimeField()
    fee = models.IntegerField()
    duration= models.IntegerField()



class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    contactno = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30,default='SOME STRING')



