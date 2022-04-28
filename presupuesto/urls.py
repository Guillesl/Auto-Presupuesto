from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "presupuesto"

urlpatterns = [
    #ex: /presupuesto/
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    ]

urlpatterns += staticfiles_urlpatterns()