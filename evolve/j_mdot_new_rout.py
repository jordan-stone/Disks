from Disks import *
from Disks import Q
import numpy as np
from Ldisk_given_Mstar_Mdisk_rout import Ldisk_given_Mstar_Mdisk_rout
from rout_given_Mstar_Mdisk_Ltot import rout_given_Mstar_Mdisk_Ltot

def j_mdot_new_rout(Mstar_0,Mdisk_0,
                    Mdot_star,j_inf,Mdot_inf,deltat,
                    rout_0=100,beta=-1,returnMstarMdisk=False,**Sigma0args):
    '''Given a keplerian disk of mass Mdisk_0 with a powerlaw density profile
    with index beta, around a star of Mstar_0 with an outer radius of rout_0,
    calculate the new disk radius after accreting mass and angular momentum from an
    envelope. Assume that the mass redistributes quickly to the powerlaw profile.
    The star increases in mass by Mdot_star*deltat the disk increases in mass by
    (Mdot_inf-Mdot_star)*delta_t
    INPUTS:
    Mstar_0   -[float] the mass of the central star in solar masses
    Mdisk_0   -[float] the total initial mass of the disk in solar masses
    Mdot_star -[float] the accretion rate onto the central star in 
                       solar masses per year
    j_inf     -[float] the specific angular momentum of infalling
                       material in cm**2/s. j_inf*Mdot_cgs gives Ldot
    Mdot_inf  -[float] the mass accretion rate onto the disk 
                       from the envelope.
    deltat    -[float] the timestep in years
    rout_0    -[float] the initial extent of the disk, in AU
    beta      -[float] the power law index of the density profile
                       Sigma \propto r**beta
    **Sigma0args - additional keywords to feed to Q.Sigma0
    RETURNS:
    rout_new in AU,
    optionally returns new Mstar and Mdisk...'''
    Mstar_0_cgs=Mstar_0*Msolar2g
    rout_0_cgs=rout_0*au2cm
    Ltot_0=Ldisk_given_Mstar_Mdisk_rout(Mstar_0,Mdisk_0,rout_0,beta=beta,**Sigma0args)

    Ltot_1=Ltot_0+(j_inf*Mdot_inf*Msolar2g*deltat)

    Mdisk_0_cgs=Mdisk_0*Msolar2g
    print '0s: ',Mstar_0,Mdisk_0,Ltot_0,beta
    Mdisk_1=Mdisk_0+(Mdot_inf-Mdot_star)*deltat
    Mdisk_1_cgs=Mdisk_1*Msolar2g

    Mstar_1=Mstar_0+(Mdot_star*deltat)
    Mstar_1_cgs=Mstar_1*Msolar2g

    print '1s: ',Mstar_1,Mdisk_1,Ltot_1,beta
    rout_1=rout_given_Mstar_Mdisk_Ltot(Mstar_1,Mdisk_1,Ltot_1,beta=beta)
    if returnMstarMdisk:
        return rout_1, Mstar_1, Mdisk_1, Ltot_1
    else:
        return rout_1
