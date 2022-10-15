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
        ("OT","OT")
    )
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, null=True)
    residential_status = models.CharField(max_length=2, choices=RESIDENTIAL_OPTIONS, null=True)
    current_address = models.CharField(max_length=100, null=True)
    national_id = models.CharField(max_length=10, unique=True, null=True)
    date_of_birth = models.DateField(null=True)
    kra_pin = models.CharField(max_length=11, unique=True, null=True)
    passport_photo = models.ImageField(blank=True, null=True)
    buyer_personal_number = models.CharField(max_length=50, null=True)
    #registeredBy
    buyers_email = models.EmailField(unique=True, null=True)
    mobile_phone = models.CharField(max_length=15, null=True)
    project_assigned = models.ManyToManyField('Plot', blank=True)
    date_of_registration = models.DateField(null=True)
    contract_type = models.CharField(choices=PAYMENT_CONTRACT, max_length=1, null=True)
    deposit_amount = models.CharField(max_length=15, null=True)
    balance_amount = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.last_name