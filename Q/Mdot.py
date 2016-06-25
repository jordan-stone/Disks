from Disks import *
import numpy as np
from Q import *

def Mdot(cs,Omega,Sigma,alpha=0.01):
    '''viscous accretion rate using \dot{M}=3\pi\nu\Sigma with 
    \nu given by \alpha*cs*h=\alpha*cs^{2}/\Omega
    inputs:
    cs    - the soundspeed in cgs
    Omega - the Keplerian angular velocity in cgs
    Sigma - the surface density in cgs
    Returns:
    mdot  - the mass accretion rate in cgs
    '''
    out = 3*np.pi*alpha*((cs**2)/Omega)*Sigma
    return out
