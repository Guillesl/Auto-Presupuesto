import numpy as np

def calcula_factor(objetos, cost_list, cost_type, info):
    
    budget_type = {'SF': "solar_field_cost",  'bop': "bop_cost", 'construc': "construction_cost", 'transport': "transport_cost", 'sto': "storage_cost"}
    cost_field = budget_type[cost_type]

    if (cost_field == "storage_cost") and (info.vol_storage == 0):
        estimated_cost=0
        a = 0
        b = 0

    else:
        num_list = "num_colect"
        if cost_field == "storage_cost":
            num_list = "vol_storage"

        num_colect_list = [getattr(i, num_list) for i in objetos]

        '''Cálculo de la referencia, dando prioridad a los proyectos reales'''
        num_colect_user = getattr(info, num_list)

        if objetos.filter(real_offer = True):
            num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
        else:
            num_colect_ref = min(num_colect_list, key=lambda j:abs(j-num_colect_user))
        
        if cost_field == "storage_cost":
            project_ref = objetos.filter(vol_storage = num_colect_ref)[0]
        else:
            project_ref = objetos.filter(num_colect = num_colect_ref)[0] #se podría añadir la condición de que sea el proyecto verdadero más reciente
        
        x = [i/num_colect_ref for i in num_colect_list]

        if (cost_field == "transport_cost"):
            project_ref_cost = getattr(project_ref, cost_field)/(num_colect_ref*project_ref.distance)
        else:
            project_ref_cost = getattr(project_ref, cost_field)

        cost_f = [i/project_ref_cost for i in cost_list]
        y = [i/j for i, j in zip(cost_f, x)]
        coefs = np.polyfit(np.log(x),np.log(y),1)

        '''y=a*x**b'''
        a = np.exp(coefs[1])                      
        b = coefs[0]

        '''Cálculo del coste del concepto del presupuesto'''
        estimated_cost = (project_ref_cost/num_colect_ref)*((a*num_colect_user/num_colect_ref)**b)*num_colect_user
        
        if (cost_field == "transport_cost"):
            estimated_cost = estimated_cost*num_colect_user*info.distance

    return round(a,3),  round(b,3), round(estimated_cost,1)