from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from presupuesto.calculations import calcula_factor
from .models import Project, Solar_field
from .forms import ProjectForm

def index(request):
    a_solar = ''
    b_solar = ''

    form = ProjectForm(request.POST or None, request.FILES or None)
    # print (form)
    
    if form.is_valid():
        form.save()
        info = Project.objects.latest("pub_date")
        a_solar = calcula_factor(Solar_field.filtro(), info)[0]
        b_solar = calcula_factor(Solar_field.filtro(), info)[1]

        return HttpResponseRedirect(reverse('presupuesto:results', args = (a_solar,)))

    return render(request, "presupuesto:index", {"a": a_solar, "b": b_solar, "form": form})


def results(request, a_solar):
    return render(request, "polls:results", {
        "a": a_solar
    })
