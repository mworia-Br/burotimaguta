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
    location=models.CharField(max_length=100)
    description=models.TextField()
    availableUnits=models.IntegerField(max_length=4)
    plotsize=models.CharField(max_length=30,choices=plotsize_choices,default="")
    nearByamenities=models.TextField()
    images=models.FileField(upload_to='plots/images/')
    sellingprice=models.IntegerField(max_length=20,null=True)
    discountprice=models.IntegerField(max_length=20,null=True)
    #userbooked=models.ManyToManyField(User,blank=True)