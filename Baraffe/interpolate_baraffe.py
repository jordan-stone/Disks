from Disks.Baraffe import *
from Disks.Baraffe import read_baraffe
from Disks.readcol import readcol
from scipy.interpolate import interp1d
import os
import numpy as np

model='BCAH98_models.1'
path,fname=os.path.split(__file__)
keys=["m","age","Teff","g","log L","Mv","Mr","Mi","Mj","Mh","Mk","Ml'","Mm"]
dat=readcol(os.path.join(path,model),colNames=keys)

def interpolate_baraffe(mass):
    if mass <= 0.02:
        data=read_baraffe(0.02,model=model)
        return data['Teff'][0], data['r'][0]
    else:
        modeled_masses=np.sort(np.unique(dat['m']))
        just_below=modeled_masses[modeled_masses<mass][-1]
        print 'JUST BELOW:', just_below
        just_above=modeled_masses[modeled_masses>mass][0]
        print 'JUST ABOVE:', just_above
        below_inds=dat["m"]==just_below
        above_inds=dat["m"]==just_above

        belowvals=map(lambda k:dat[k][below_inds],keys)
        belowdict=dict(zip(keys,belowvals))
        belowdict['r']=R_from_T_and_L(dat["Teff"],10**dat["log L"])

        abovevals=map(lambda k:dat[k][above_inds],keys)
        abovedict=dict(zip(keys,abovevals))
        abovedict['r']=R_from_T_and_L(dat["Teff"],10**dat["log L"])

        below_Teff=belowdict["Teff"][0]
        print 'BELOW TEFF: ',below_Teff
        above_Teff=abovedict["Teff"][0]
        print 'ABOVE TEFF: ',above_Teff

        below_L=10**belowdict["log L"][0]
        above_L=10**abovedict["log L"][0]

        out_Teff=interp1d([just_below,just_above],[below_Teff,above_Teff])(mass)
        out_L=interp1d([just_below,just_above],[below_L,above_L])(mass)
        out_R=R_from_T_and_L(out_Teff,out_L)
        return float(out_Teff), float(out_R)

    
