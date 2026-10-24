from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField()
    semester = models.CharField()
    password = models.CharField(max_length=8)
