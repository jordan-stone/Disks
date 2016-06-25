import numpy as np
import matplotlib.pyplot as mpl
from readcol import readcol
from scipy.interpolate import NearestNDInterpolator as nn
from scipy.interpolate import LinearNDInterpolator as ll
from scipy.interpolate import griddata
import os

def get_Ferguson_opacity(T,density=10**-16.1,OpacityFname='g7.02.tron'):
    path,fname=os.path.split(__file__)
    d=readcol(os.path.join(path,OpacityFname),colNames=(['T']+list(np.linspace(-8,1,19))))
    log_rhos={}
    xy=[]
    z=[]
    for k in np.linspace(-8,1,19):
        log_rhos[k]=np.log10(((10**(d['T']-6))**3)*(10**k))
        xy.extend(zip(d['T'],log_rhos[k]))
        z.extend(10**d[k])
    func=nn(np.array(xy),np.array(z))
    return func(np.log10(T),np.log10(density))

def get_Ferguson_opacity_linear(T,density=10**-16.1,OpacityFname='g7.02.tron'):
    path,fname=os.path.split(__file__)
    d=readcol(os.path.join(path,OpacityFname),colNames=(['T']+list(np.linspace(-8,1,19))))
    log_rhos={}
    xy=[]
    z=[]
    for k in np.linspace(-8,1,19):
        print k
        log_rhos[k]=np.log10(((10**(d['T']-6))**3)*(10**k))
        xy.extend(zip(d['T'],log_rhos[k]))
        z.extend(10**d[k])
    mpl.scatter([x[0] for x in xy],[y[1] for y in xy],c=z)
    mpl.show()
    func=ll(np.array(xy),np.array(z))
    print np.array(xy)[:2,:], np.array(z)[:2]
    return func(np.log10(T),np.log10(density))

