from re import M
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#from buyers.models import BuyerInfo

plotsize_choices= (
    ("40*90","40*90"),
    ("50*100","50*100"),
    ("100*100","100*100")
)

class Plot(models.Model):
    projectName=models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    seller=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.TextField()
    nearbyAmenities=models.TextField()
    availableUnits=models.IntegerField(null=True)
    plotsize=models.CharField(max_length=30,choices=plotsize_choices,default="")
    images=models.FileField(upload_to='plots/projectimages/')
    sellingprice=models.IntegerField(null=True)
    discountprice=models.IntegerField(null=True)
    deposit=models.IntegerField(null=True)
    #userbooked=models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.projectName


class Plot_Number(models.Model):
    project = models.ForeignKey(Plot, on_delete=models.CASCADE)
    plotNumber = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    imageonMap = models.FileField(upload_to='plots/plotimages/',null=True)
    price = models.IntegerField()
    bookedby = models.ForeignKey('buyers.BuyerInfo',on_delete=models.CASCADE, null=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.plotNumber
