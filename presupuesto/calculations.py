import numpy as np


def calcula_factor(objetos, info):
    num_colect_list = [i.num_colect for i in objetos]
    cost_colect_list = [i.cost for i in objetos]
    
    '''Cálculo de la referencia'''
    num_colect_user = info.num_colect
    #vol_storage_user = form.vol_storage

    if objetos.filter(real_offer = True):
        num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
    else:
        num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
    
    project_ref = objetos.filter(num_colect=num_colect_ref)[0]
    x = [i/num_colect_ref for i in num_colect_list]
    cost_f = [i/project_ref.cost for i in cost_colect_list]
    y = [i/j for i, j in zip(cost_f, x)]
    coefs = np.polyfit(np.log(x),np.log(y),1)
    #scipy.optimize.curve_fit(lambda t,b: np.exp(b*t),  x,  y)

    '''y=a*x**b'''
    a = np.exp(coefs[1])                      
    b = coefs[0]

    return a, b