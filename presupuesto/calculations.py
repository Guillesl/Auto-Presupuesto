import numpy as np

def calcula_factor(objetos, cost_list, cost_type, info):
    
    budget_type = {'SF': "solar_field_cost",  'bop': "bop_cost", 'construc': "construction_cost", 'transport': "transport_cost", 'sto': "storage_cost"}
    cost_field = budget_type[cost_type]

    if (cost_field == "storage_cost") and (info.vol_storage == 0):
        estimated_cost=0
        a = 0
        b = 0

    else:
        num_colect_list = [i.num_colect for i in objetos]

        '''Cálculo de la referencia, dando prioridad a los proyectos reales'''
        num_colect_user = info.num_colect
        #vol_storage_user = form.vol_storage

        if objetos.filter(real_offer = True):
            num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
        else:
            num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
        
        project_ref = objetos.filter(num_colect=num_colect_ref)[0] #se podría añadir la condición de que sea el proyecto verdadero más reciente
        x = [i/num_colect_ref for i in num_colect_list]
        cost_f = [i/getattr(project_ref, cost_field) for i in cost_list]
        y = [i/j for i, j in zip(cost_f, x)]
        coefs = np.polyfit(np.log(x),np.log(y),1)
        #scipy.optimize.curve_fit(lambda t,b: np.exp(b*t),  x,  y)

        '''y=a*x**b'''
        a = np.exp(coefs[1])                      
        b = coefs[0]

        '''Cálculo del coste del campo solar'''
        estimated_cost = (getattr(project_ref, cost_field)/num_colect_ref)*((a*num_colect_user/num_colect_ref)**b)*num_colect_user


    return round(a,3),  round(b,3), round(estimated_cost,1)