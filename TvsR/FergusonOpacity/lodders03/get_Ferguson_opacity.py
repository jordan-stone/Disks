import numpy as np
from readcol import readcol
from scipy.interpolate import NearestNDInterpolator as nn
from scipy.interpolate import LinearNDInterpolator as ll
from scipy.interpolate import griddata
import os

def get_Ferguson_opacity_linear(T,density=10**-16.1,OpacityFname='l03.7.02.tron'):
    path,fname=os.path.split(__file__)
    d=readcol(os.path.join(path,OpacityFname),colNames=(['T']+list(np.linspace(-8,1,19))))
    rhos={}
    xy=[]
    z=[]
    for k in np.linspace(-8,1,19):
        print k
        rhos[k]=((10**(d['T']-6))**3)*(10**k)
        xy.extend(zip(10**d['T'],rhos[k]))
        z.extend(10**d[k])
    func=ll(np.array(xy),np.array(z),rescale=True)
    print np.array(xy)[:2,:], np.array(z)[:2]
    return func(T,density)

