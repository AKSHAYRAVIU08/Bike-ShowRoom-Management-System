from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Register(AbstractUser):
    pass;


class Send(models.Model):
    customer_name=models.CharField(max_length=40, null=True, blank=True)
    district=models.CharField(max_length=40, null=True, blank=True)
    purpose=models.CharField(max_length=40, null=True, blank=True)