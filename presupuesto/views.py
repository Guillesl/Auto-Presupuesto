from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from presupuesto.calculations import calcula_factor
from .models import Project, Solar_field
from .forms import ProjectForm

def index(request):
    return render(request, 'presupuesto/index.html', {"form": ProjectForm})

def results(request):
    a_solar = ''
    b_solar = ''
    # if(request.method == 'GET'):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        info = form.save(commit=False)
        a_solar = calcula_factor(Solar_field.filtro(), info)[0]
        #b_solar = calcula_factor(Solar_field.filtro(), info)[1]

        return render(request, "presupuesto/results.html", {"a": a_solar})
    
    else:
        return render(request, 'presupuesto/index.html')

