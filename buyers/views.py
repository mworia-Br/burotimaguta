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
    return render(request, 'burotimaguta/buyers.html', {'buyers':buyers,'buyers_form': form})


def create_buyer(request):
    if request.method == 'POST':
        form = BuyersForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Buyer added booking successfuly initiated")
            return redirect('burotimaguta:buyers')
        else:
            messages.error(request, "Error adding buyer")

    else:
        form = BuyersForm()

    return render(request, 'burotimaguta/buyer.html', {'buyers_form': form})


def buyer_detail(request, buyer_id):
    buyer = get_object_or_404(BuyerInfo, pk=buyer_id)
    return render(request, 'burotimaguta/buyer_detail.html', {'buyer': buyer})


def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Payment recorded successfully")
            return HttpResponseRedirect('/payments')
        else:
            messages.error(request, "Error recording payment")
    else:
        form = PaymentForm()

    return render(request, 'buyers/payment.html', {'form': form})

def edit_payment(request, payment_id):
    payment = get_object_or_404(BuyerPayments, id=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)

        if form.is_valid():
            form.save()
            messages.success(request, "Payment updated successfully")
            return HttpResponseRedirect('/payments')
        else:
            messages.error(request, "Error updating payment")
    else:
        form = PaymentForm(instance=payment)

    return render(request, 'burotimaguta/edit_payment.html', {'form': form})


def delete_payment(request, payment_id):
    payment = get_object_or_404(BuyerPayments, id=payment_id)
    payment.delete()
    messages.success(request, "Payment deleted successfully")
    return HttpResponseRedirect('/payments')




def all_payments(request):
    payments = BuyerPayments.objects.all()

    return render(request, 'burotimaguta/payments.html', {'payments': payments})


def buyer_edit(request, buyer_id):
    buyer = BuyerInfo.objects.get(id=buyer_id)
    return render(request, 'buyer_update_form.html', {'buyer': buyer})


def buyer_update(request, buyer_id):
    buyer = BuyerInfo.objects.get(id=buyer_id)

    if request.method == 'POST':
        form = BuyersForm(request.POST, instance=buyer, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "buyer updated successfully")
            return redirect("/buyers")
        else:
            messages.error(request, "error updating the buyer")
    else:
        form = BuyersForm(instance=buyer)
    return render(request, 'burotimaguta/buyer_update_form.html', {'buyer': buyer, 'buyer_form': form})      