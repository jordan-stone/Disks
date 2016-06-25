from Disks.TvsR import *
from Disks.Baraffe import read_baraffe
import matplotlib.pyplot as mpl
import numpy as np

#6000,1500,600,300,50,10,2
#even as few as 2 sampled ts seems to result in the same curve...
d=read_baraffe(0.02)
a=np.linspace(0.006,1,1000)
tr,mdotr=active_and_irradiated_combined_opacity(a,0.002,d['r'][0],d['Teff'][0],sampled_ts=np.linspace(10,3000,10))
mpl.plot(tr,'r-')
tr0,mdotr0=active_and_irradiated_semenov_opacity(a,0.002,d['r'][0],d['Teff'][0],sampled_ts=np.linspace(10,3000,10))
mpl.plot(tr0,'b-')
