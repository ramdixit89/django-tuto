from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField()
    email = models.EmailField()
    course = models.CharField()
    semester = models.IntegerField()
    password = models.CharField()

    def _str_(self):
        self.name

