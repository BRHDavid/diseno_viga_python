import connect_to_etabs as ce
import geometry_material as gm
import get_moments_etabs as ge
import pandas as pd

diametro_de_barras = {'1/4': 0.64,
                      '3/8': 0.9525, 
                      '1/2': 1.27, 
                      '5/8': 1.59, 
                      '3/4': 1.91, 
                      '1': 2.54}
rebar = {"As(cm2) +": [],
         "As(cm2) -": []}

SapModel = ce.connect_to_etabs()
geometry_material = gm.geometry_material(SapModel)
momentos = ge.m_abs_max()
diametro_prueba_long = diametro_de_barras["5/8"] #diametro_de_barras[input("Ingresa el diámetro del acero longitudinal: ")]
diametro_prueba_estribo = diametro_de_barras["3/8"] #diametro_de_barras[input("Ingresa el diámetro del estribo: ")]
recubrimiento = 4#float(input("Recubrimiento (cm): "))

def acero():
    for i in range(len(geometry_material)):
        d = geometry_material["ALTURA (cm)"][i] -recubrimiento-diametro_prueba_estribo-diametro_prueba_long/2
        a = d/5
        dif = 1
        while dif != 0:
            as_iteracion = (momentos["M +"][i] * 100000) / (
                        0.9 * geometry_material["f'y (kg/cm2)"][i] * (
                (d - (a / 2))))
            K = (as_iteracion * geometry_material["f'y (kg/cm2)"][i]) / (
                        0.85 * geometry_material["f'c (kg/cm2)"][i] * geometry_material["BASE (cm)"][i])
            K = round(K, 2)
            dif = abs(K - a)
            a = K
        as_iteracion = round(as_iteracion, 3)
        rebar["As(cm2) +"].extend([as_iteracion])
        dif = 1
        while dif != 0:
            as_iteracion = (momentos["M -"][i] * 100000) / (
                        0.9 * geometry_material["f'y (kg/cm2)"][i] * (
                (d - (a / 2))))
            K = (as_iteracion * geometry_material["f'y (kg/cm2)"][i]) / (
                        0.85 * geometry_material["f'c (kg/cm2)"][i] * geometry_material["BASE (cm)"][i])
            K = round(K, 2)
            dif = abs(K - a)
            a = K
        as_iteracion = round(as_iteracion, 3)
        rebar["As(cm2) -"].extend([as_iteracion])
    return pd.DataFrame(rebar)

if __name__ == "__main__":
    print(acero())


    
    
