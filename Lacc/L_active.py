from Disks import *
import numpy as np

def L_active(Mstar,Mdot,Rstar,rin=0.0056,rout=300):
    '''Integrate the active disk luminosity from rin to rout
    T_disk^4=[3GMstarMdot/(8*pi*sigma*r^3)]*(1-(Rstar/r)^0.5)
    L(r)=4*pi*r*sigma*T_disk^4*dr#4pirdr becuase of 2 sides...
    Ltot=integral(4*pi*r*sigma*[3GMstarMdot/(8*pi*sigma*r^3)]*(1-(Rstar/r)^0.5)dr,rin,rout)
        =integral(3/2 * GMMdot/r^2 * (1-(Rstar/r)^0.5)dr,rin,rout)
    Ltot=3/2 * GMMdot [2/3*sqrt(Rstar/r^3)-1/r]_{rin}^{rout}

    Inputs:
    Mstar - the mass of the star in solar masses
    Mdot  - the mass accretion rate in solar masses per year
    Rstar - the radius of the star in solar radii
    rin   - [optional, default=0.5] the inner radius of the 
            disk for the integration in AU
    rout  - [optional, default=300] the outer radius of the 
            disk for the integraion in AU
    '''
    Mstar_cgs=Mstar*Msolar2g
    Mdot_cgs=Mdot*Msolar2g/year2second
    Rstar_cgs=Rstar*Rsolar2cm
    rin_cgs=rin*au2cm
    rout_cgs=rout*au2cm

    first_term=((Rstar_cgs/rout_cgs**3)**0.5)-1/rout_cgs
    second_term=((Rstar_cgs/rin_cgs**3)**0.5)-1/rin_cgs
    return G*Mstar_cgs*Mdot_cgs*(first_term-second_term)

