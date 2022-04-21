from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from presupuesto.calculations import calcula_factor
from .models import Construction, Solar_field, Balance_Of_Plant, Storage, Transport
from .forms import ProjectForm

def index(request):
    return render(request, 'presupuesto/index.html', {"form": ProjectForm})

def results(request):
    # if(request.method == 'GET'):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        info = form.save(commit=False)
        budget_solar = calcula_factor(Solar_field.filtro(), [i.solar_field_cost for i in Solar_field.filtro()], "SF", info)
        a_solar = budget_solar[0]
        b_solar = budget_solar[1]
        SF_cost = budget_solar[2]

        budget_bop = calcula_factor(Balance_Of_Plant.filtro(info.integration, info.fluid), [i.bop_cost for i in Balance_Of_Plant.filtro(info.integration, info.fluid)], "bop",info)
        a_bop = budget_bop[0]
        b_bop = budget_bop[1]
        bop_cost = budget_bop[2]

        budget_construc = calcula_factor(Construction.filtro(info.surface), [i.construction_cost for i in Construction.filtro(info.surface)], "construc",info)
        a_const = budget_construc[0]
        b_const = budget_construc[1]
        const_cost = budget_construc[2]

        budget_transport = calcula_factor(Transport.filtro(info.vehicule), [i.transport_cost for i in Transport.filtro(info.vehicule)], "transport",info)
        a_transp = budget_transport[0]
        b_transp = budget_transport[1]
        transp_cost = budget_transport[2]

        budget_storage = calcula_factor(Storage.filtro(info.fluid), [i.storage_cost for i in Storage.filtro(info.fluid)], "sto",info)
        a_sto = budget_storage[0]
        b_sto = budget_storage[1]
        sto_cost = budget_storage[2]

        return render(request, "presupuesto/results.html", {
            "a_solar": a_solar, "b_solar": b_solar, "SF_cost": SF_cost,
            "a_bop": a_bop, "b_bop": b_bop, "bop_cost": bop_cost,
            "a_const": a_const, "b_const": b_const, "const_cost": const_cost,
            "a_transp": a_transp, "b_transp": b_transp, "transp_cost": transp_cost,
            "a_sto": a_sto, "b_sto": b_sto, "sto_cost": sto_cost,
            })
    
    else:
        return render(request, 'presupuesto/index.html')

