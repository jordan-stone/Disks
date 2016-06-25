from Disks import *
from Disks import Q
import numpy as np

def Ldisk_given_Mstar_Mdisk_rout(Mstar,Mdisk,rout,
                                 rin=0.005,beta=-1,**Sigma0args):
    '''Calculate the total angular momentum of a smooth Keplerian disk. The
    disk has mass Mdisk, distributed between rin and rout with a powerlaw index
    of beta.
    INPUTS:
    Mstar   -[float] the mass of the central star in solar masses
    Mdisk   -[float] the total mass of the disk in solar masses
    rin     -[float] the inner extent of the disk, in AU
    rout    -[float] the outer extent of the disk, in AU
    beta      -[float] the power law index of the density profile
                       Sigma \propto r**beta
    **Sigma0args - additional keywords to feed to Q.Sigma0
    RETURNS:
    Ltot, the total angular momentum of the disk
    optionally returns new Mstar and Mdisk...'''
    Mstar_cgs=Mstar*Msolar2g
    rout_cgs=rout*au2cm
    rin_cgs=rin*au2cm
    Sigma0=Q.Sigma0(Mdisk,beta=beta,rin=rin,rout=rout,**Sigma0args)#rin shows up here
    normalization=Sigma0*2*np.pi*((G*Mstar_cgs)**0.5)*au2cm**(-1*beta)
    Ltot=normalization*( ( (rout_cgs**(2.5+beta))/(2.5+beta) )
                          -( ( rin_cgs**(2.5+beta))/(2.5+beta) ))#rin shows up here, too...
    return Ltot
