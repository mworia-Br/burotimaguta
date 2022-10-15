from pyexpat.errors import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
from buyers.forms import BuyersForm, PaymentForm
from buyers.models import BuyerInfo, BuyerPayments


def buyers(request):
    buyers = BuyerInfo.objects.all()
    if request.method == 'POST':
        form = BuyersForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Buyer added booking successfuly initiated")
        else:
            messages.error(request, "Error adding buyer")
    else:
        form = BuyersForm()
    return render(request, 'buyers/buyers.html', {'buyers':buyers,'buyers_form': form})


def record_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Payment recorded successfully")
            return HttpResponseRedirect('/payments')
        else:
            messages.error(request, "Error recording payment")
    else:
        form = PaymentsForm()

    return render(request, 'buyer/payments.html', {'form': form})        