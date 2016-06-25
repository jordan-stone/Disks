from Disks import *
import numpy as np
from Disks.Q import *

def Q(c,Omega,Sigma):
    '''Toomre's Q:
    inputs:
    c     - the (isothermal) sound speed in cm/s
    Omega - the Keplerian angular velocity in radians/sec
    Sigma - the surface density in g/cm^2
    '''
    return c*Omega/(np.pi*G*Sigma)
