# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirects
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from plots.models import Plot, Plot_Number

