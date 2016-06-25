from Disks.Baraffe import *
from readcol import readcol
import numpy as np
import os

def read_baraffe(mass,model='BCAH98_models.1'):
    path,fname=os.path.split(__file__)
    keys=["m","age","Teff","g","log L","Mv","Mr","Mi","Mj","Mh","Mk","Ml'","Mm"]
    dat=readcol(os.path.join(path,model),colNames=keys)
    inds=dat["m"]==mass
    if inds.sum()==0:
        print "mass must be one of: ",np.unique(dat["m"])
    goodvals=map(lambda k:dat[k][inds],keys)
    dat.update(zip(keys,goodvals))
    dat['r']=R_from_T_and_L(dat["Teff"],10**dat["log L"])
    return dat

