from django.db import models


# Create your models here.
GENDER_CHOICES=[
    ("FEMALE",'F'),
    ("MALE", 'M'),
    ("OTHERS", 'O'),
]

class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username
