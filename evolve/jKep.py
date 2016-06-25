from Disks import *
from Disks.Q import Omega

def jKep(Mstar,a):
    '''Return the specific angular momentum
    of an object in keplerian orbit with a 
    semi-major axis a around a central mass
    of mass Mstar.
    INPUTS:
    Mstar - the central mass in solar masses
    a     - the semi major axis in AU
    RETURNS:
    jKep  - the specific angular momentum associated with
            this orbit.'''
    return ((a*au2cm)**2)*Omega(Mstar,a)
