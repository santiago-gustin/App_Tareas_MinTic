from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    #COMENTAR EN CASO DE NECESIDAD PARA CREAR MAS SUPERUARIOS

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []