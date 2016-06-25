import matplotlib.pyplot as mpl
import numpy as np
from readcol import readcol
from plottingTools.fixplotsImproved import custom_settings,compModern, tickFont
import matplotlib.gridspec as gridspec
custom_settings()

fname='g7.02.tron'
d=readcol(fname,colNames=(['T']+list(np.linspace(-8,1,19))))
log_rhos={}
xy=[]
z=[]
for k in np.linspace(-8,1,19):
    log_rhos[k]=np.log10(((10**(d['T']-6))**3)*(10**k))
    xy.extend(zip(d['T'],log_rhos[k]))
    z.extend(10**d[k])
f=mpl.figure()
gs=gridspec.GridSpec(20,20)
a=f.add_subplot(gs[:,:18])
foo=a.scatter([x[0] for x in xy],[y[1] for y in xy],c=np.log10(z),lw=0)
cax=f.add_subplot(gs[:,18:])
cbar=mpl.colorbar(foo,cax=cax)
cbar.set_label(r'log$_{10}$ $\kappa$',fontproperties=compModern(20))
a.set_xlabel(r'log$_{10}$ T',fontproperties=compModern(25))
a.set_ylabel(r'log$_{10}$ $\rho$',fontproperties=compModern(25))
a.set_ylim(ymin=-18.9)
tickFont(a,'x',compModern(20))
tickFont(a,'y',compModern(20))
mpl.tight_layout()
mpl.tight_layout()
mpl.tight_layout()
