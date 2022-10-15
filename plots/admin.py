from django.contrib import admin
# Register your models here.
from .models import Plot,Plot_Number

admin.site.register(Plot,Plot_Number)
