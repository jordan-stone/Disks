import numpy as np
from readcol import readcol
from scipy.interpolate import interp1d
import os

path,fname=os.path.split(__file__)
data=readcol(os.path.join(path,'kPkR.dat'),colNames=['T','P161','R161','P125','R125'])
R_low_func=interp1d(data['T'],data['R161'])
R_high_func=interp1d(data['T'],data['R125'])
P_low_func=interp1d(data['T'],data['P161'])
P_high_func=interp1d(data['T'],data['P125'])

def get_Semenov_opacity(T,density=10**-16.1,Rosseland=True):
    '''Get the disk opacity according to the iron-poor silicate model of
    Semenov et al. 2003 models.  This function interpolates between temperature
    and density. The density interpolation is probably not what we want, and
    density=10**-16.1 or density=10**-12.5 should be used
    inputs:
    T         - the temperature of the medium in Kelvin
    density   - the volumetric density in g/cm^3
    Rosseland - (bool) True to use the Rosseland mean, False to use the Planck 
                mean opacity'''
    if Rosseland==True:
       low_density=R_low_func(T)
       high_density=R_high_func(T)
       delta_density=(density-10**-16.1)/(10**-12.5-10**-16.1)
       return low_density+(high_density-low_density)*delta_density
    elif Rosseland==False:
       low_density=P_low_func(T)
       high_density=P_high_func(T)
       delta_density=(density-10**-16.1)/(10**-12.5-10**-16.1)
       return low_density+(high_density-low_density)*delta_density
