from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuName = models.CharField(max_length=70)
    stuEmail = models.CharField(max_length=70)
    stuPass = models.CharField(max_length=16)

    # def __str__(self):
    #     return self.stuName