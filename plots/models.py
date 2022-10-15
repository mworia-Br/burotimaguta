from re import M
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

plotsize_choices= (
    ("50*100","50*100")
    ("100*100","100*100")
)

class Plot(models.Model):
    projectName=models.CharField(max_length=100)
    seller=models.CharField(max_length=100)