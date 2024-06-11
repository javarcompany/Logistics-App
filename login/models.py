from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(verbose_name="User name", max_length = 30, unique = True)
    email = models.EmailField(verbose_name="Email Address", unique=True)
    phone = models.CharField(verbose_name="Phone Number", max_length=13, blank = True, null = True)
    img = models.ImageField(upload_to='users/')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username