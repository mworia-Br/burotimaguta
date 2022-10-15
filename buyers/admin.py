from django.contrib import admin
# Register your models here.
from .models import BuyerInfo, BuyerPayments

admin.site.register(BuyerInfo)
admin.site.register(BuyerPayments)