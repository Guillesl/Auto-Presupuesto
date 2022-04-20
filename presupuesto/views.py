from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from presupuesto.calculations import calcula_factor
from .models import Construction, Project, Solar_field
from .forms import ProjectForm

def index(request):
    return render(request, 'presupuesto/index.html', {"form": ProjectForm})

def results(request):
    # if(request.method == 'GET'):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        info = form.save(commit=False)
        budget_solar = calcula_factor(Solar_field.filtro(), [i.solar_field_cost for i in Solar_field.filtro()], info)
        a_solar = budget_solar[0]
        b_solar = budget_solar[1]
        SF_cost = budget_solar[2]

        budget_construc = calcula_factor(Construction.filtro(info.surface), [i.construction_cost for i in Construction.filtro(info.surface)], info)
        a_const = budget_construc[0]
        b_const = budget_construc[1]
        const_cost = budget_construc[2]

        return render(request, "presupuesto/results.html", {
            "a_solar": a_solar, "b_solar": b_solar, "SF_cost": SF_cost,
            "a_const": a_const, "b_const": b_const, "const_cost": const_cost
            })
    
    else:
        return render(request, 'presupuesto/index.html')

