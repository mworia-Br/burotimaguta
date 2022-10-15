from django.db import models

# Create your models here.
from plots.models import Plot


class BuyerModel(models.Model):
    GENDER_OPTIONS =(
        ("M","Male")
        ("F","Female")
        ("O","Other")
    )

    RESIDENTIAL_OPTIONS = (
        ('R','Resident')
        ("NR","Non-Resident")
    )

    PAYMENT_CONTRACT = (
        ("Deposit + 3months","Deposit + 3months")
        ("Deposit + 6months","Deposit + 6months")
        ("Deposit + 12months","Deposit + 12months")
        ("Deposit + 24months","Deposit + 24months")
        ("One time","One time")
    )