from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Project, Solar_field

def index(request):
    a = Solar_field.calcula_factor()[0]
    b = Solar_field.calcula_factor()[1]
    return render(request, "presupuesto/index.html", {"a": a, "b": b})