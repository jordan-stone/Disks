from Disks import *
import numpy as np
from Disks.Q import *

def Omega(Mstar,a):
    '''Keplerian angular velocity assuming circular orbit.
    inputs:
    Mstar - Mass of the star in solar masses
    a     - semimajor axis of orbit in AU
    '''
    Mstar_cgs=Mstar*Msolar2g
    a_cgs=a*au2cm
    return (G*Mstar_cgs/(a_cgs**3))**0.5
