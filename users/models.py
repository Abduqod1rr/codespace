from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(models.Model,AbstractUser):
    ROLE_CHOICES=[
        ('dev','Dev'),
        ('viewer','Viewer')
        
    ]
    role =  models.CharField(choices=ROLE_CHOICES,default='dev')
    
    def __str__(self):
        return f"{self.username},{self.role}"