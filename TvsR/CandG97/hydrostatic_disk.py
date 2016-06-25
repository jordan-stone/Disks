from Disks import *
from Disks.TvsR.CandG97 import *

def hydrostatic_disk(Mstar,Rstar,Tstar,a):#equation 1, 5, 8, and 10...
    '''Temperature at a radius a for a hydrostatic disk, using
    Chiang and Goldreich (1997) eqns 1, 5, 8, and 10.
    inputs:
    Mstar - stellar mass in solar Masses
    Rstar - stellar radius in solar Radii
    a     - stellocentric radius in in au'''
    alph=alpha(a,Rstar,Tstar,Mstar)
    Rstar_cgs=Rstar*Rsolar2cm
    a_cgs=a*au2cm
    return ((alph/2.)**0.25) * ((Rstar_cgs/a_cgs)**0.5) * Tstar
    

