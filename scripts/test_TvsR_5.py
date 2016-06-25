from Disks.TvsR import *
from Disks.Baraffe import read_baraffe
import matplotlib.pyplot as mpl
import numpy as np

#6000,1500,600,300,50,10,2
#even as few as 2 sampled ts seems to result in the same curve...
colors=('r','g','b','c','m','k')
for ii,m in enumerate((0.02,0.03,0.04,0.05,0.08)):
    d=read_baraffe(m)
    a=np.linspace(Rsolar2au*d['r'][0]*5,1,300)
    print 'combined'
    tr,mdotr=active_and_irradiated_combined_opacity(a,m,d['r'][0],d['Teff'][0],sampled_ts=np.linspace(10,3000,10))
    mpl.plot(a,tr,colors[ii]+'-')
    print 'semenov'
    tr0,mdotr0=active_and_irradiated_semenov_opacity(a,m,d['r'][0],d['Teff'][0],sampled_ts=np.linspace(10,3000,10))
    mpl.plot(a,tr0,colors[ii]+'--')
