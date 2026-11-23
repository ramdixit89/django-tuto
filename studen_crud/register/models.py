
from django.db import models


class User(models.Model):

    # Field 1: Name of the student
    name = models.CharField(max_length=100)

    # Field 2: Unique email
    email = models.EmailField(blank=True, unique=True)

    # Field 3: Course choices dropdown
    course = models.CharField(
        max_length=10,
        default='bca',
        choices=[
            ('bca', 'BCA'),
            ('bsc', 'BSc'),
        ]
    )

    # Field 4: Semester dropdown
    semester = models.IntegerField(
        choices=[
            (1, '1'),
            (3, '3'),
            (5, '5')
        ]
    )

    # Field 5: Password
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
