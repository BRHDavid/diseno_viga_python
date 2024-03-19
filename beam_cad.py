from pyautocad import Autocad, aDouble
from pyautocad import APoint as AP
import connect_to_etabs as ce
import beam_etabs as be

acad = Autocad()
a = acad.doc.Utility.GetPoint()
point_insert = AP(a[0], a[1], 0)
viga = be.Viga()
longitud = viga.longitud()
peralte = viga.peralte()

for i in range(len(longitud)):
    if i % 2 == 0:
        point1 = AP(a[0], a[1] + peralte[i], 0)
        acad.model.AddLine(point_insert, point1)
    else: 
        point1 = AP(a[0] + longitud[i-1], a[1] + peralte[i], 0)
        acad.model.AddLine(point_insert, point1)
    



