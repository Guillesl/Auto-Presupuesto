import datetime
from re import A

from django.db import models
from django.utils import timezone
from scipy.optimize import curve_fit
import numpy as np

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

    def best_reference(self, num_colect, vol_storage):
        '''Select the reference based on the REAL proyect with most similar number of collectors and storage volume'''
        num_colect_ref = 60
        #vol_storage_ref = 5000
        return num_colect_ref #, vol_storage_ref


class Solar_field(Project):
    a = float
    b = float

    def __init__(self, num_colect, cost, real_offer, num_colect_ref, pub_date, a, b):
        super.__init__(num_colect, cost, real_offer, num_colect_ref, pub_date)

        '''Calculation of the scale factor, sería interesante crear una función'''
        num_colect_list = [self.num_colect for i in self.objects.all()]
        cost_colect_list = [self.cost for i in self.objects.all()]

        x = [i/self.num_colect_ref for i in num_colect_list]
        cost_f = [i/self.objects.get(num_colect=num_colect_ref) for i in cost_colect_list]
        y = [cost_f/x for i in zip(cost_f, x)]
        coefs = np.polyfit(np.log(x),np.log(y),1)

        '''y=a*x**b'''
        self.a = np.exp(coefs[1])                      
        self.b = coefs[0]


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
