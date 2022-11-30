from django.db import models
import numpy as np
import pandas as pd
# Create your models here.


class MemberData(models.Model):
    firstname = models.CharField(max_length=30, default='First name')
    lastname = models.CharField(max_length=30, default='Last name')
    username = models.CharField(max_length=50, default='User name', primary_key=True)
    email = models.CharField(max_length=30, default='email')
    password = models.CharField(max_length=50, default='password')

