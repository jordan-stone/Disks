import numpy as np
from readcol import readcol
from scipy.interpolate import interp1d
import os

def get_Semenov_opacity(T,density=10**-16.1,Rosseland=True,
                        OpacityFname='kPkR.dat'):
    '''Get the disk opacity according to the iron-poor silicate model of
    Semenov et al. 2003 models.  This function interpolates between temperature
    and density. The density interpolation is probably not what we want, and
    density=10**-16.1 or density=10**-12.5 should be used
    inputs:
    T         - the temperature of the medium in Kelvin
    density   - the volumetric density in g/cm^3
    Rosseland - (bool) True to use the Rosseland mean, False to use the Planck 
                mean opacity'''
    path,fname=os.path.split(__file__)
    d=readcol(os.path.join(path,OpacityFname),colNames=['T','P161','R161','P125','R125'])
    if Rosseland==True:
       low_density=interp1d(d['T'],d['R161'])(T)
       high_density=interp1d(d['T'],d['R125'])(T)
       delta_density=(density-10**-16.1)/(10**-12.5-10**-16.1)
       return low_density+(high_density-low_density)*delta_density
    elif Rosseland==False:
       low_density=interp1d(d['T'],d['P161'])(T)
       high_density=interp1d(d['T'],d['P125'])(T)
       delta_density=(density-10**-16.1)/(10**-12.5-10**-16.1)
       return low_density+(high_density-low_density)*delta_density
