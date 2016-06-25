from Disks import *
import numpy as np
from Disks.Q import *

def Sigma0(Mdisk,beta=-1,rin=0.005,rout=100):
    '''Calculate the surface density at 1 AU for a disk with 
    powerlaw index beta and mass Mdisk. Start the derivation 
    using dm=2*pi*r*Sigma(r)dr and substitute Sigma(r) with 
    Sigma0*(r/r0)^beta, r0=1AU...
    Inputs:
    Mdisk - the total mass of the disk in solar masses
    beta  - the powerlaw index of the surface density distribution
    rin   - the inner radius of the disk in AU
    rout  - the outer radius of the disk in AU
    Returns:
    Sigma0 - the surface density at 1AU in g/cm^2
    '''
    Mdisk_cgs=Mdisk*Msolar2g
    rin_cgs=rin*au2cm
    rout_cgs=rout*au2cm
    return ( (beta+2) * Mdisk_cgs )/( (2*np.pi*au2cm**(-1*beta))*( (rout_cgs**(beta+2))-(rin_cgs**(beta+2)) ) )
