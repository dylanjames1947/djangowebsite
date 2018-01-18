from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Organization, Contracts, Company
from .forms import LoginForm, RegisterForm, RegisterContracts


def index(request):
    allContracts = Contracts.objects.all()
    context = {
        'allContracts': allContracts,
    }
    return render(request, 'register/index.html', context)


def agencydetails(request, agency_id):
    return HttpResponse("<h1> Agency number : " + str(agency_id) + "</h1>")


def sign_in(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)
        c.save()
    return render(request, 'register/login-register.html', {'form': form})


def CreateContracts(request):
    form = RegisterContracts(request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)
        c.save()
    return render(request, 'register/Contracts_form.html', {'form': form})