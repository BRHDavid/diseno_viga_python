import connect_to_etabs as ce
import pandas as pd

SapModel = ce.connect_to_etabs()
SapModel.SetPresentUnits(12) #Tn-m-c
SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
SapModel.Results.Setup.SetComboSelectedForOutput("Envolvente")
data = SapModel.Results.FrameForce("",3,0)

def data_beam():
    beam_forces = pd.DataFrame(data[1:14],index= ["Name",
                                                    "1",
                                                    "2",
                                                    "Station",
                                                    "4",
                                                    'Step Type',
                                                    '6','P',
                                                    'V2','V3',
                                                    'T','M2','M3']).transpose()
    eliminar = ["1","2","4",'6','P','V2','V3','T','M2']
    beam_m3 = beam_forces.drop(columns=eliminar)
    SapModel = None
    return beam_m3

if __name__ == "__main__":
    print(data_beam())
