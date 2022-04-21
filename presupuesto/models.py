import datetime
from mimetypes import init

from django.db import models
from django.utils import timezone

integration_choices = (
    ('SL_S_FW','SL_S_FW'),
    ('SL_S_FWS', 'SL_S_FWS'),
    ('SL_S_PD','SL_S_PD'),
    ('SL_S_PD+FWS','SL_S_PD+FWS'),
    ('SL_L_P','SL_L_P'),
    ('SL_L_PS','SL_L_PS'),
    ('SL_L_RF','SL_L_RF'),
    ('SL_L_S','SL_L_S'),		
)

fluid_choices = (
    ('steam', 'steam'),
    ('water', 'water'),
    ('oil', 'oil'),
)

surface_choices = (
    ('roof_concrete', 'cubierta de hormigón'),
    ('roof_sandwich', 'cubierta sandwich'),
    ('ground_paved', 'suelo asfaltado'),
    ('ground_unpaved', 'suelo no asfaltado'),
)

transport_choices = (
    ('truck', 'camión'),
    ('ship', 'barco'),
)

class Project(models.Model):

    name = models.CharField(max_length=200)
    num_colect = models.IntegerField()
    vol_storage = models.BigIntegerField()
    integration = models.CharField(max_length=15, choices=integration_choices)
    fluid = models.CharField(max_length=15, choices=fluid_choices)
    dist_supply = models.IntegerField()
    surface = models.CharField(max_length=30, choices=surface_choices)
    vehicule = models.CharField(max_length=15, choices=transport_choices)
    distance = models.BigIntegerField()
    pressure = models.IntegerField()
    cost = models.BigIntegerField()
    solar_field_cost = models.BigIntegerField()
    bop_cost = models.BigIntegerField()
    construction_cost = models.BigIntegerField()
    transport_cost = models.BigIntegerField()
    storage_cost = models.BigIntegerField()
    real_offer = models.BooleanField()
    pub_date = models.DateField("date published")
    
    def __str__(self):
        return self.name

class bop(models.Model):
    pass
    # fluido = 
    # tipo_integracion = 
    # numero_colectores  = 
    # presupuesto = 
    

class Solar_field(Project):
    def __init__(self, name, num_colect, solar_field_cost, real_offer, pub_date):
        super.__init__(name, num_colect, solar_field_cost, real_offer, pub_date )

    def filtro():
        projects = Project.objects.all()
        return projects

class Balance_Of_Plant(Project):
    def __init__(self, name, num_colect, integration, fluid, dist_supply, bop_cost, real_offer, pub_date):
        super.__init__(name, num_colect, integration, fluid, dist_supply, bop_cost, real_offer, pub_date )

    def filtro(integration_choice, fluid_choice):
        projects = Project.objects.filter(integration = integration_choice, fluid = fluid_choice)
        return projects

class Construction(Project):
    def __init__(self, name, num_colect, surface, construction_cost, real_offer, pub_date):
        super.__init__(name, num_colect, surface, construction_cost, real_offer, pub_date )

    def filtro(surface_choice):
        projects = Project.objects.filter(surface = surface_choice)
        return projects   

class Transport(Project):
    def __init__(self, name, num_colect, vehicule, distance, transport_cost, real_offer, pub_date):
        super.__init__(name, num_colect, vehicule, distance, transport_cost, real_offer, pub_date)

    def filtro(vehicule_choice):
        projects = Project.objects.filter(vehicule = vehicule_choice)
        return projects   

class Storage(Project):
    def __init__(self, name, fluid, vol_storage, integration, pressure, storage_cost, real_offer, pub_date):
        super.__init__(name, fluid, vol_storage, integration, pressure, storage_cost, real_offer, pub_date )

    def filtro(fluid_choice):
        projects = Project.objects.filter(fluid = fluid_choice)
        return projects