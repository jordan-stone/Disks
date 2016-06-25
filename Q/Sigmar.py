from Disks import *
import numpy as np
from Disks.Q import *

def Sigmar(Mdisk,a,**sigma0kwargs):
    '''Calculate the surface density at a radius a in a disk of total mass 
    Mdisk
    Input:
    Mdisk - the total mass of the disk in solar masses
    a     - the radius in AU at which to evaluate the surface density
    Returns:
    the surface density in g/cm^2
    '''
    S0=Sigma0(Mdisk,**sigma0kwargs)
    return S0*a**sigma0kwargs['beta']
