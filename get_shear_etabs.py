import pandas as pd
import results_beam_cortante as rbc

beam_v2 = rbc.data_beam()
names = beam_v2["Name"].unique()

for i in names:
    v2_max = beam_v2[(beam_v2["Name"]==i) & (beam_v2["Step Type"]=="Max")]
    v2_max = v2_max["V2"].max()
    
    v2_min = beam_v2[(beam_v2["Name"]==i) & (beam_v2["Step Type"]=="Min")]
    v2_min = v2_min["V2"].min()
    
    v2 = max(v2_max, abs(v2_min))
    
    
