from Disks.TvsR import *
from Disks.Baraffe import read_baraffe
import matplotlib.pyplot as mpl
import numpy as np

#6000,1500,600,300,50,10,2
#even as few as 2 sampled ts seems to result in the same curve...
d=read_baraffe(0.05)
a=np.linspace(0.1,100,1000)
tr,mdotr=active_and_irradiated_semenov_opacity(a,0.05,d['r'][0],d['Teff'][0],sampled_ts=np.linspace(10,3000,100))
mpl.plot(tr)
tr0,mdotr0=active_and_irradiated_semenov_opacity(a,0.05,d['r'][0],d['Teff'][0],sampled_ts=np.linspace(10,3000,2))
mpl.plot(tr0)
