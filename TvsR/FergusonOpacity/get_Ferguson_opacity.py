import numpy as np
from readcol import readcol
from scipy.interpolate import LinearNDInterpolator as ll
import os

#right now this only returns Rosseland opacities. Ferguson does provide one file with planck opacities, but
#it is not with the same abundances... what to do. skip it for now.
path,fname=os.path.split(__file__)
OpacityFname='GN93/g7.02.tron'
d=readcol(os.path.join(path,OpacityFname),colNames=(['T']+list(np.linspace(-8,1,19))))
log_rhos={}
xy=[]
z=[]
for k in np.linspace(-8,1,19):
    log_rhos[k]=np.log10(((10**(d['T']-6))**3)*(10**k))
    xy.extend(zip(d['T'],log_rhos[k]))
    z.extend(10**d[k])
func=ll(np.array(xy),np.array(z))

def get_Ferguson_opacity(T,density=10**-14):
    kappa=func(np.log10(T),np.log10(density))
    if np.any(np.isnan(kappa)):
        raise ValueError("you're outside of the convex-hull of the ferguson opacity data T=%f,rho=%e"%(T,density))
    else:
        return kappa

