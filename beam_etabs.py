import connect_to_etabs as ce
import results_beam as rb
import geometry_material as ge

SapModel = ce.connect_to_etabs()
SapModel.SetPresentUnits(12)


class Viga:
    """Las dimensiones estan en cm"""
    def peralte(self):
        data_geometry = ge.geometry_material(SapModel)
        name_geometry = data_geometry["VIGA"].unique()
        self.altura = []
        for i in name_geometry:
            self.altura.append(data_geometry[(data_geometry["VIGA"]==i)].iloc[-1]["ALTURA (cm)"]/100)
        return self.altura
    
    def longitud(self):
        data_long = rb.data_beam()
        name_long = data_long["Name"].unique()
        self.l = []
        for i in name_long:
             self.l.append(data_long[(data_long["Name"]==i) & 
                           (data_long['Step Type'] == "Min")].iloc[-1]["Station"])
        return self.l
    
class Columna:
    def select(self):
        select = SapModel.SelectObj.GetSelected()[2:4]
    
if __name__ == "__main__":
    viga1 = Viga()
    Viga.peralte(viga1)
    Viga.longitud(viga1)
    SapModel = None



