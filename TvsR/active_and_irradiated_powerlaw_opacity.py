from Disks import *
from Disks.TvsR.CandG97 import alpha, hydrostatic_disk
from Disks.Lacc import Lacc as Lacc_func
from Disks.Q import Sigmar as Sigmar_func
from Disks.Q import Omega as Omega_func
from Disks.Q import cfromT, Sigma_active, Mdot
from scipy.optimize import newton
import numpy as np

def active_and_irradiated_powerlaw_opacity(a,Mstar,Mdot,Rstar,Tstar,
                          diskMassFrac=0.01,kappa0_r=2.5e-4,kappa0_p=2.5e-4):
    '''Calculate T vs. R for a disk including contributions from irradiation
    (from the star and the accretion shock onto the star), and from viscous
    dissapation. The equation I use is a modification of eq 18 in Kratter et al. 2008, that
    also incorporates the contribution of the accretion shock irradiation.
    The equation is:

    \sigmaT_{disk}^4=(((8/6)*Sigma*kappa0_r*T^2)+(1/(2*Sigma*kappa0_p*T^2)))*F_{nu}+F_{irr},

    where F_{nu} is the flux from an active disk defined elsewhere in these codes (see
    Lacc.L_active), and F_{irr}=F_{star}+F_{acc}

    Inputs:
    a            -  The radius, in [AU], at which to find the temperature.
    Mstar        -  The mass of the central object in [Msolar]
    Mdot         -  The accretion rate, in [Msolar/year], onto the central object
    Rstar        -  The radius, in [Rsolar], of the central star
    Tstar        -  The effective temperature of the central object
    diskMassFrac -  The total mass of the circumstellar disk as a [fraction of Mstar]
    kappa0_r     -  The normalization of the Rosseland opacity powerlaw
    Kappa0_p     -  The normalization of the Planck opacity powerlaw
    '''

    a_au=a
    a_cgs=a*au2cm
    Rstar_sol=Rstar
    Rstar_cgs=Rstar*Rsolar2cm
    Mstar_sol=Mstar
    Mstar_cgs=Mstar*Msolar2g
    Mdot_sol=Mdot
    Mdot_cgs=Mdot*Msolar2g/year2second

    alphas=alpha(a_au,Rstar_sol,Tstar,Mstar_sol)#radians...
    Sigmar=Sigmar_func(Mstar_sol*diskMassFrac,a_au,beta=-1,rin=0.005,rout=100.)#g/cm^2

    Lstar=4*np.pi*((Rstar_cgs)**2)*stephan_boltzmann*Tstar**4#ergs/s
    Lacc=Lacc_func(Mstar_sol,Rstar_sol,Mdot_sol)#ergs/s

    F_active=(3/(8*np.pi))*(Mdot_cgs)*(Omega_func(Mstar_sol,a_au)**2)*(1-np.sqrt(Rstar_cgs/a_cgs))#ergs/s/cm^2

    A=(8./6.)*Sigmar*kappa0_r*F_active
    B=(0.5/(Sigmar*kappa0_p))*F_active
    C=(alphas/2.)*(Lstar+Lacc)/(4*np.pi*a_cgs**2)
    first_guesses=hydrostatic_disk(Mstar_sol,Rstar_sol,Tstar,a_au)

    Tr=np.array([],dtype=float)
    for params in zip(A,B,C,first_guesses):
        def func(T):
            #return (stephan_boltzmann*T**4)-(params[0]*T**2)-(params[1]*T**-2)-params[2]
            return (stephan_boltzmann*T**4)-(params[0]*T**2)-params[2]
        try:
            temp=newton(func,params[-1])
        except:
            temp=newton(func,100.*params[-1])
            
        Tr=np.r_[Tr,temp]
    return Tr
