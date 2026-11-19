from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, unique=True)
    course = models.CharField(default='BCA', choices=[
                                    ('bca', 'BCA'),
                                    ('bsc', 'BSc'),
                                ])
    semester = models.IntegerField(choices=[
                                         (1,'1'), 
                                         (3,'3'), 
                                         (5,'5')
                                ])
    password = models.CharField()

    def __str__(self):
        return self.name

