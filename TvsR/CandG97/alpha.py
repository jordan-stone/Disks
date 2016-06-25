from Disks import *
from Disks.TvsR.CandG97 import *

def alpha(a,Rstar,Tstar,Mstar):
    '''the grazing angle at radius a for a hydrostatic disk,
    combining Chiang and Goldreich (1997) eqns. 10, 8, and 5
    input:
    a     - the stellocentric radius in AU
    Rstar - The stellar radius in solar radii
    Tstar - the stellar temperature in Kelvin
    Mstar - The stellar mass in solar masses'''
    tc=Tc(Mstar,Rstar)
    a_cgs=a*au2cm
    Rstar_cgs=Rstar*Rsolar2cm
    return (0.4*Rstar_cgs/a_cgs) + (8./7.) * ((Tstar/tc)**(4./7.)) * (a_cgs/Rstar_cgs)**(2./7.)

