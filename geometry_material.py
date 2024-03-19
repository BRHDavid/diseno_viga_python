import connect_to_etabs as ce
import pandas as pd
SapModel = ce.connect_to_etabs()

def geometry_material(SapModel):
    """Los datos obtenido estan en
    Fuerza --> Kg
    Distancia -->cm """
    SapModel.SetPresentUnits(12)
    select = SapModel.SelectObj.GetSelected()[2]
    data = {
        "VIGA":[],
        "f'c (kg/cm2)":[],
        "f'y (kg/cm2)":[],
        "BASE (cm)":[],
        "ALTURA (cm)":[],
        "As min":[]
    }
    for i in select:
        section_label = SapModel.FrameObj.GetSection(i)[0]
        get_data = SapModel.PropFrame.GetRectangle(section_label)[1:4]
        get_rebar_name = SapModel.PropFrame.GetRebarBeam(section_label)[0]
        fc = SapModel.PropMaterial.GetOConcrete(get_data[0])[0]
        fy = SapModel.PropMaterial.GetORebar(get_rebar_name)[0]
        as_min = (0.7*fc**(1/2)/fy)*get_data[2]*100*get_data[1]*100
        for j in range(3):
            data["VIGA"].append(f"VIGA {i}")
            data["f'c (kg/cm2)"].append(fc/10)
            data["f'y (kg/cm2)"].append(fy/10)
            data["BASE (cm)"].append(get_data[2]*100)
            data["ALTURA (cm)"].append(get_data[1]*100)
            data["As min"].append(as_min)
            
    data_df = pd.DataFrame(data)
    return data_df

if __name__ == "__main__":
    print(geometry_material(SapModel))