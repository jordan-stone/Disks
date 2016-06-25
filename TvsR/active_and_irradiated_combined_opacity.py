import matplotlib.pyplot as mpl
from Disks import *
from Disks.TvsR.CandG97 import alpha
from Disks.TvsR.zero_find import zero_find
from Disks.Lacc import Lacc as Lacc_func
from Disks.TvsR import get_combined_opacity as kappa
from Disks.Q import Sigmar as Sigmar_func
from Disks.Q import Omega as Omega_func
from Disks.Q import cfromT, Sigma_active, Mdot
import numpy as np

def first_term(T):
    return (stephan_boltzmann*T**4)
def second_term(T,Sigmaa,F_active):
    return (8./6.)*Sigmaa*F_active*kappa(T)
def third_term(T,Sigmaa,F_active):
    return ((0.5/Sigmaa)*F_active)/kappa(T,Rosseland=False)
def fourth_term(T,alpha_min,Lstar,Lacc,amin):
    return (alpha_min/2.)*(Lstar+Lacc)/(4*np.pi*(amin*au2cm)**2)

#density is not yet being passed to kappa. the defualt density is being used for all opacity function calls...
def active_and_irradiated_combined_opacity(a,Mstar,Rstar,Tstar,
                                          diskMassFrac=0.01,amin=None,aout=100.,sampled_ts=np.linspace(10,3000,5),zero_find_default=10.):
    '''Calculate T vs. R for a disk including contributions from irradiation
    (from the star and the accretion shock onto the star), and from viscous
    dissapation. The equation I use is a modification of eq 18 in Kratter et al. 2008, that
    also incorporates the contribution of the accretion shock irradiation.
    The equation is:

    \sigmaT_{disk}^4=(((8/6)*Sigma*kappa_r(T))+(1/(2*Sigma*kappa_p(T))))*F_{nu}+F_{irr},

    where F_{nu} is the flux from an active disk defined elsewhere in these codes (see
    Lacc.L_active), and F_{irr}=F_{star}+F_{acc}. kappa_r(T) and kappa_p(T) are the 
    temperature dependent Rosseland and Planck mean opacities from Semenov et al. (2003)
    Inputs:
    a            -  The radius, in [AU], at which to find the temperature.
    Mstar        -  The mass of the central object in [Msolar]
    Rstar        -  The radius, in [Rsolar], of the central star
    Tstar        -  The effective temperature of the central object
    diskMassFrac -  The total mass of the circumstellar disk as a [fraction of Mstar]
    amin         -  The minimum radius of the disk, this is used to derive the accretion
                    rate onto the star which is a term used in deriving irradiation Luminosity.
    sampled_ts   -  The temperatures to sample on the curve to begin the zero-finding process.
    Returns:
    (Tr,Mr)      -  The eemperature as a function of radius and the accretion rate as 
                    a function of radius in a tuple
    '''

    a_au=a
    a_cgs=a*au2cm
    Rstar_sol=Rstar
    Rstar_cgs=Rstar*Rsolar2cm
    Mstar_sol=Mstar
    Mstar_cgs=Mstar*Msolar2g
    if amin==None:
        amin=np.array([5*Rsolar2au*Rstar_sol])
    else:
        amin=np.array([amin])

    #Define the parameters which do not depend on mdot or T
    alphas=alpha(a_au,Rstar_sol,Tstar,Mstar_sol)#radians...
    alpha_min=alpha(amin,Rstar_sol,Tstar,Mstar_sol)#radians...
    Lstar=4*np.pi*((Rstar_cgs)**2)*stephan_boltzmann*Tstar**4#ergs/s

    #make a first guess at the accretion rate which
    #makes it onto the star (which we assume is the same
    #as the accretion rate at the inner edge of the disk).
    #Also, calculate the accretion luminosity, given the 
    #assumed accretion rate.
    mdot0=1e-10
    Lacc=Lacc_func(Mstar_sol,Rstar_sol,mdot0)#ergs/s

    #iterate to converge on the mass accretion rate at inner 
    #rim/onto star for proper calculation of Lacc.
    new_sampled_ts=sampled_ts
    while True:
        print 'inner loop'
        #Define the governing equation using the current guess of mdot and Lacc...
        #the function expects T to be iterable...
        def thefunc(T,returnTerms=False):
            Sigmar=Sigmar_func(Mstar_sol*diskMassFrac,amin,beta=-1,rin=amin[0],rout=aout)
            Sigmaa=Sigma_active(Sigmar,T)
            cs=cfromT(T)
            Mdot_cgs=Mdot(cs,Omega_func(Mstar_sol,amin),Sigmaa)
            F_active=(3/(8*np.pi))*(Mdot_cgs)*(Omega_func(Mstar_sol,amin)**2)*(1-np.sqrt(Rstar_cgs/(amin*au2cm)))

            first_term=(stephan_boltzmann*T**4)
            second_term=(8./6.)*Sigmaa*F_active*kappa(T)
            third_term=((0.5/Sigmaa)*F_active)/kappa(T,Rosseland=False)
            fourth_term=(alpha_min/2.)*(Lstar+Lacc)/(4*np.pi*(amin*au2cm)**2)
            #f=mpl.figure()
            #a=f.add_subplot(111)
            #a.plot(first_term,label='1st')
            #a.plot(second_term,label='2nd')
            #a.plot(third_term,label='3rd')
            #a.plot(fourth_term,label='4th')
            #a.legend()
            #mpl.show()
            if returnTerms:
                return float(first_term-second_term-third_term-fourth_term), first_term,second_term,third_term,fourth_term
            else:
                return float(first_term-second_term-third_term-fourth_term)

        rim_temp=zero_find(thefunc,new_sampled_ts,default=zero_find_default)
        print 'rim_temp: ',rim_temp
        #use temperature to calculate new mdot
        print 'Mdot c,omega,sigma: '
        print cfromT(rim_temp),Omega_func(Mstar_sol,amin),Sigma_active(Sigmar_func(Mstar_sol*diskMassFrac,amin,beta=-1,rin=amin[0],rout=aout),rim_temp)

        mdot_rim=Mdot(cfromT(rim_temp),
                        Omega_func(Mstar_sol,amin),
                        Sigma_active(Sigmar_func(Mstar_sol*diskMassFrac,amin,beta=-1,rin=amin[0],rout=aout),rim_temp))
        mdot_rim=(mdot_rim/Msolar2g)*year2second
        print 'mdot_rim: ',mdot_rim
        #Check if converged
        if mdot_rim-mdot0<(0.0001*mdot0):
            break
        #not converged. update guesses.
        mdot0=mdot_rim
        Lacc=Lacc_func(Mstar_sol,Rstar_sol,mdot0)#ergs/s
        new_sampled_ts=np.linspace(rim_temp-100,rim_temp+100,10)


    #set accretion luminosity using the mdot derived for the inner rim.
    Lacc=Lacc_func(Mstar_sol,Rstar_sol,mdot_rim)#ergs/s
    Tr=np.array([],dtype=float)
    Mr=np.array([],dtype=float)
    for ra in zip(a_au,alphas):
        print 'current radius: ',ra[0]
        def thefunc(T):
            Sigmar=Sigmar_func(Mstar_sol*diskMassFrac,np.array([ra[0]]),beta=-1,rin=amin[0],rout=aout)
            #Sigmaa=np.concatenate(map(lambda t:Sigma_active(Sigmar,t),T))
            Sigmaa=Sigma_active(Sigmar,T)
            Mdot_cgs=Mdot(cfromT(T),Omega_func(Mstar_sol,ra[0]),Sigmaa)
            F_active=(3/(8*np.pi))*(Mdot_cgs)*(Omega_func(Mstar_sol,ra[0])**2)*(1-np.sqrt(Rstar_cgs/(ra[0]*au2cm)))

            first_term=(stephan_boltzmann*T**4)
            second_term=(8./6.)*Sigmaa*F_active*kappa(T)
            third_term=((0.5/Sigmaa)*F_active)/kappa(T,Rosseland=False)
            fourth_term=(ra[1]/2.)*(Lstar+Lacc)/(4*np.pi*(ra[0]*au2cm)**2)
            
            return float(first_term-second_term-third_term-fourth_term)
        Tr=np.r_[Tr,zero_find(thefunc,sampled_ts,default=zero_find_default)]
    Sigmaa=np.array(map(lambda a,t:Sigma_active(Sigmar_func(Mstar_sol*diskMassFrac,a,beta=-1,rin=amin[0],rout=aout),t),a_au,Tr))
    Mr=Mdot(cfromT(Tr),Omega_func(Mstar_sol,a_au),Sigmaa)
    return (Tr,Mr)
