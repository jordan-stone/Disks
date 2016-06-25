from Disks import *
import numpy as np

def active_disk(r,Mstar=1.,Mdot=1.e-8,Rstar=1.):
    '''Calculate TvsR for an actively accreting disk, using 
    Frank, King, and Raine eqn. 5.43
    Inputs:
    r      - The radius in AU
    Mstar - The stellar mass in solar masses
    Mdot  - The accretion rate in solar masses per year
    Rstar - The stellar radius in solar radii

    Returns:
    the temperature at r in Kelvins...
    '''
    r_cgs=r*au2cm
    Mstar_cgs=Mstar*Msolar2g
    Mdot_cgs=Mdot*Msolar2g*1./year2second
    Rstar_cgs=Rstar*Rsolar2cm

    first_term=3*G*Mstar_cgs*Mdot_cgs/(8.*np.pi*stephan_boltzmann*r_cgs**3)
    second_term=(1-np.sqrt(Rstar_cgs/r_cgs))
    return (first_term*second_term)**0.25

