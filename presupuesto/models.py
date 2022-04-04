import datetime
import numpy as np

from django.db import models
from django.utils import timezone
from scipy.optimize import curve_fit

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
    transport = models.CharField(max_length=15, choices=transport_choices)
    distance = models.BigIntegerField()
    pressure = models.IntegerField()
    cost = models.BigIntegerField()
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
    

class Solar_field(models.Model):
    def __init__(self):
        self.projects = Project.objects.all()
        return self.projects

    def calcula_factor():
        num_colect_list = [i.num_colect for i in Project.objects.all()]
        cost_colect_list = [i.cost for i in Project.objects.all()]
       
        '''Cálculo de la referencia'''
        if Project.objects.filter(real_offer = True):
            num_colect_user = 60 #FALTA QUE SE ENLACE CON LA VIEW PARA QUE EL USUARIO INTRODUZCA EL VALOR
            num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))

        else:
            num_colect_user = 60
            num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
        
        project_ref = Project.objects.get(num_colect=num_colect_ref)
        x = [i/num_colect_ref for i in num_colect_list]
        cost_f = [i/project_ref.cost for i in cost_colect_list]
        y = [i/j for i, j in zip(cost_f, x)]
        coefs = np.polyfit(np.log(x),np.log(y),1)
        #scipy.optimize.curve_fit(lambda t,b: np.exp(b*t),  x,  y)

        '''y=a*x**b'''
        a = np.exp(coefs[1])                      
        b = coefs[0]

        return a, b


# class Balance_Of_Plant(Project):
        # def scale_factor_calculation(self):
        # scale_factor = self.objects.filter()
#     pass

# class Construction(Project):
#     pass

# class Transport(Project):
#     pass

# class Storage(Project):
#     pass
