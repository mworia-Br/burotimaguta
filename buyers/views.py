#from pyexpat.errors import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from buyers.forms import BuyersForm, PaymentForm
from buyers.models import BuyerInfo, BuyerPayments
from plots.models import Plot, Plot_Number


@login_required(login_url='/accounts/login/')
def index(request):
    projects = Plot.objects.all()
    project_count = projects.count()

    plots = Plot_Number.objects.all()
    plot_count = plots.count()

    buyers = BuyerInfo.objects.all()
    buyers_count = buyers.count()

    payments = BuyerPayments.objects.all()
    payment_count = payments.count()

    return render(request, 'buyers/index.html',{'buyers_count': buyers_count, 'payment_count': payment_count, 'project_count': project_count, 'plot_count': plot_count})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def create_buyer(request):
    if request.method == 'POST':
        form = BuyersForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Buyer added booking successfuly initiated")
            return redirect('buyers:buyers')
        else:
            messages.error(request, "Error adding buyer")

    else:
        form = BuyersForm()

    return render(request, 'buyers/buyer.html', {'buyers_form': form})


@login_required(login_url='/accounts/login/')
def buyer_detail(request, buyer_id):
    buyer = get_object_or_404(BuyerInfo, pk=buyer_id)
    return render(request, 'buyers/buyer_detail.html', {'buyer': buyer})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
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

    return render(request, 'buyers/edit_payment.html', {'form': form})


@login_required(login_url='/accounts/login/')
def delete_payment(request, payment_id):
    payment = get_object_or_404(BuyerPayments, id=payment_id)
    payment.delete()
    messages.success(request, "Payment deleted successfully")
    return HttpResponseRedirect('/payments')


@login_required(login_url='/accounts/login/')
def all_payments(request):
    payments = BuyerPayments.objects.all()

    return render(request, 'buyers/payments.html', {'payments': payments})


@login_required(login_url='/accounts/login/')
def buyer_edit(request, buyer_id):
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
    return render(request, 'buyer_update_form.html', {'buyer': buyer})


@login_required(login_url='/accounts/login/')
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
    return render(request, 'buyers/buyer_update_form.html', {'buyer': buyer, 'buyer_form': form})      