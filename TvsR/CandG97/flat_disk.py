from Disks import *
from Disks.TvsR.CandG97 import *

def flat_disk(Tstar,Rstar,a):#equation 4
    '''Chiang and Goldreich (1997) equation 4, 
    a flat disk with each annulus emitting as a blackbody.
    input:
    Tstar - the stellar temperature in Kelvin
    Rstar - the stellar radius in solar radii
    a     - the stellocentric radius in au'''
    Rstar_cgs=Rstar*Rsolar2cm
    a_cgs=a*au2cm
    return (2./(3*np.pi))**(0.25)*(Rstar_cgs/(a_cgs))**(0.75)*Tstar
