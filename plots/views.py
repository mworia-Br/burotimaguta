# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from plots.models import Plot, Plot_Number


@login_required(login_url='/accounts/login/')
def plots(request):
    plots = Plot.objects.all()
    """
    if request.method == 'POST':
        form = plotsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "plot added booking successfuly initiated")
        else:
            messages.error(request, "Error adding plot")
    else:
        form = plotsForm()
    """    
    return render(request, 'plots/plots.html', {'plots':plots})


@login_required(login_url='/accounts/login/')
def plot_detail(request, plot_id):
    plot = get_object_or_404(Plot, pk=plot_id)
    return render(request, 'plots/plot_detail.html', {'plot': plot})


@login_required(login_url='/accounts/login/')
def all_plotnumbers(request):
    plotnumbers = Plot_Number.objects.all()

    return render(request, 'plots/plotnumbers.html', {'plotnumbers': plotnumbers})


@login_required(login_url='/accounts/login/')
def plotnumber_detail(request, plotnumber_id):
    plotnumber = get_object_or_404(Plot_Number, pk=plotnumber_id)
    return render(request, 'plotnumbers/plotnumber_detail.html', {'plotnumber': plotnumber})