from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    rolechoices=(
        ('ADMIN','Admin'),
        ('USER','User'),
    )
    role=models.CharField(max_length=50,choices=rolechoices,default='USER')
