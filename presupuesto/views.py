from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from . import calculations

from .models import Project, Solar_field

def index(request):
    scale_factor = calculations.best_reference()
    return render(request, "presupuesto/index.html", {
        "scale_factor": scale_factor})