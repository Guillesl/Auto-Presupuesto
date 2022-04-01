import numpy as np

from .models import Solar_field

def best_reference():
    '''Select the reference based on the REAL proyect with most similar number of collectors and storage volume'''
    num_colect_ref = 60
    #vol_storage_ref = 5000

    # '''Calculation of the scale factor, sería interesante crear una función'''
    # num_colect_list = [Solar_field.num_colect for i in Solar_field.objects.all()]
    # cost_colect_list = [Solar_field.cost for i in Solar_field.objects.all()]

    # x = [i/num_colect_ref for i in num_colect_list]
    # cost_f = [i/Solar_field.objects.get(num_colect=num_colect_ref) for i in cost_colect_list]
    # y = [cost_f/x for i in zip(cost_f, x)]
    # coefs = np.polyfit(np.log(x),np.log(y),1)

    # '''y=a*x**b'''
    # a = np.exp(coefs[1])                      
    # b = coefs[0]

    return num_colect_ref