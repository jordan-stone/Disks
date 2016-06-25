from Disks import *
import numpy as np

def Lacc(Mstar,Rstar,Mdot,Rin=3.):
    '''Accretion shock luminosity:
    Inputs:
    Mstar - The mass of the star in solar masses
    Rstar - the Radius of the star in solar radii
    Mdot  - The accretion rate onto the star in solar masses per year
    Rin   - [optional default=3] The inner radius of the accretion disk
            in units of the STELLAR radius (i.e. not solar radii)
    '''
    Mstar_cgs=Mstar*Msolar2g
    Rstar_cgs=Rstar*Rsolar2cm
    Mdot_cgs=Mdot*Msolar2g/year2second
    return 0.5*(G*Mstar_cgs*Mdot_cgs/Rstar_cgs)*(1.-1./Rin)

