from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    message = models.TextField(200)





# Create your models here.
