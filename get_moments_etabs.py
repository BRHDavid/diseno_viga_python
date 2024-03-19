import pandas as pd
import connect_to_etabs as ce
import results_beam_momentos as rb
import geometry_material as gm
beam_m3 = rb.data_beam()

def m_abs_max():
    """
    - Obtener los 6 momentos de diseño:
    - Los valores retornados estan en 
        -->Fuerza   : Tn
        -->Distancia: m
    - Se debe tener el combo Envolvente definido en etabs"""
    
    names = beam_m3["Name"].unique()
    lista_momentos = {"M +":[],
                      "M -": []}
    for i in names:
        filtrado_neg = beam_m3[(beam_m3["Name"]==i)
                            & (beam_m3['Step Type'] == "Min")]
        filtrado_pos = beam_m3[(beam_m3["Name"]==i)
                            & (beam_m3['Step Type'] == "Max")]
        filas_neg = len(filtrado_neg)
        filas_pos = len(filtrado_pos)
        #Para los momentos negativos
        ini_neg = abs(filtrado_neg.iloc[0]["M3"])
        int_neg = abs(filtrado_neg.iloc[filas_neg//2]["M3"])
        end_neg = abs(filtrado_neg.iloc[filas_neg-1]["M3"])
        #Para los momentos positivos
        ini_pos = abs(filtrado_pos.iloc[0]["M3"])
        int_pos = abs(filtrado_pos.iloc[filas_pos//2]["M3"])
        end_pos = abs(filtrado_pos.iloc[filas_pos-1]["M3"])
        """Tratamiento de momentos para Vigas de 
        porticos especiales ACI 318-19"""
        ini_pos, end_pos  = max(ini_pos, ini_neg*0.5), max(end_pos, end_neg*0.5)
        maximo = max(ini_neg, end_neg, ini_pos, end_pos)
        int_neg, int_pos = max(int_neg, maximo*0.25), max(int_pos, maximo*0.25)
        
        lista_momentos["M -"].extend([ini_neg, int_neg, end_neg])
        lista_momentos["M +"].extend([ini_pos, int_pos, end_pos])
    
    momentos_finales_df = pd.DataFrame(lista_momentos)
    return momentos_finales_df

if __name__ == "__main__":
    print(m_abs_max())

    