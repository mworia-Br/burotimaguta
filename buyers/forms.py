from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm
from buyers.models import BuyerInfo, BuyerPayments
from crispy_forms.layout import Field, Layout, Div, ButtonHolder, Submit


class BuyersForm(ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    date_of_registration = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))


    class Meta:
        model = BuyerInfo
        fields = "__all__"


class PaymentForm(ModelForm):
    class Meta:
        model = BuyerPayments
        fields = "__all__"