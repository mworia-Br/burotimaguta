from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm
from buyers.models import BuyerInfo, BuyerPayments
from crispy_forms.layout import Field, Layout, Div, ButtonHolder, Submit


class BuyersForm(ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    date_of_registration = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(Field('first_name'), css_class='col-md-4', ),
                Div(Field('last_name'), css_class='col-md-4', ),
                Div(Field('middle_name'), css_class='col-md-4', ),
                Div(Field('gender'), css_class='col-md-4', ),
                Div(Field('date_of_birth'), css_class='col-md-4', ),
                Div(Field('residential_status'), css_class='col-md-4', ),
                Div(Field('current_address'), css_class='col-md-4', ),
                Div(Field('national_id'), css_class='col-md-4', ),
                css_class='row',
            ),
            Div(
                Div(Field('kra_pin'), css_class='col-md-4', ),
                Div(Field('passport_photo'), css_class='col-md-4', ),
                Div(Field('buyer_personal_number'), css_class='col-md-4', ),
                Div(Field('buyers_email'), css_class='col-md-4', ),
                Div(Field('mobile_phone'), css_class='col-md-4', ),
                Div(Field('date_of_registration'), css_class='col-md-4', ),
                Div(Field('project_assigned'), css_class='col-md-4', ),
                css_class='row',
            ),
            Div(
                Div(Field('plot_booked'), css_class='col-md-4', ),
                Div(Field('contract_type'), css_class='col-md-4', ),
                Div(Field('deposit_amount'), css_class='col-md-4', ),
                Div(Field('balance_amount'), css_class='col-md-4', ),
                Div(Field('registeredBy'), css_class='col-md-4', ),
                css_class='row',
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='button white')
            )
        )
        super(BuyersForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BuyerInfo
        fields = "__all__"


class PaymentForm(ModelForm):
    class Meta:
        model = BuyerPayments
        fields = "__all__"