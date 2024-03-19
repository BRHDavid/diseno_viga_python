import connect_to_etabs as ce
import get_moments_etabs as ge
import geometry_material as gm
import rebar_calculation as rc
import pandas as pd

SapModel= ce.connect_to_etabs()
momentos = ge.m_abs_max()
geometria_material = gm.geometry_material(SapModel)
acero = rc.acero()

def export_to_excel():
    data = pd.concat([geometria_material,
                        momentos,
                        acero], axis=1)
    try:
        data.to_excel("prueba01.xlsx", index=False)
    except:
        print("Error al momento de exportar")
export_to_excel()
    






