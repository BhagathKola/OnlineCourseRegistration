from django.db import models

# Create your models here.


class CourseregModel(models.Model):
    cid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=49)
    faculty=models.CharField(max_length=49)
    date = models.DateField()
    time =models.TimeField()
    fee = models.IntegerField()
    duration= models.CharField(max_length=50)



class StudentlogModel(models.Model):
    sid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    contactno = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)


class studentCourse(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.IntegerField()
    cid = models.IntegerField()



