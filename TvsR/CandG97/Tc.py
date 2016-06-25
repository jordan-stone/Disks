from Disks import *
from Disks.TvsR.CandG97 import *

def Tc(Mstar,Rstar,mu=1.77):#equation 8
    '''Tc equation 8 in C&G.
    input:
    Mstar - The stellar mass in solar masses
    Rstar - The stellar radius in solar radii
    mu    - The mean molecular weight of the gas in amu
            the default value, 1.77, has been tuned so that
            the C&G value ~8e6 is returned for their model 
            parameters: 0.5 M_sun, 2.5 R_sun...'''
    Mstar_cgs=Mstar*Msolar2g
    Rstar_cgs=Rstar*Rsolar2cm
    mu_cgs=mu*amu2g
    return G*Mstar_cgs*mu_cgs/(k_boltzmann*Rstar_cgs)
