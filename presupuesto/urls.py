from django.urls import path

from . import views

app_name = "presupuesto"

urlpatterns = [
    #ex: /presupuesto/
    path("", views.index, name="index"),
    ]