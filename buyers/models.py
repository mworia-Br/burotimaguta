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
        ()
    )