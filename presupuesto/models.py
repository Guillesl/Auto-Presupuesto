import datetime
from re import A

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



class Solar_field(Project):
    def __init__(self, num_colect, cost, real_offer, pub_date):
        super().__init__(num_colect, cost, real_offer, pub_date)




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
