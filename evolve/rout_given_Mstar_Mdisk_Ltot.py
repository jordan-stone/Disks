from Disks import *
from Disks import Q
import numpy as np
from scipy.optimize import brentq
def rout_func(rout,Mstar=None,Mdisk=None,Ltot=None,rin=None,beta=-1):
    '''This function is designed to be fed to a zero-finder
    to calculate the outer radius of a keplerian disk given a
    disk mass Mdisk, a stellar mass of Mstar, and a total angular
    momentum content of Ltot. 
    MATH: The expression can be derived, by integrating to find the mass of the
    disk in terms of Sigma0, rin and rout, and also integrating to find the
    total angular momentum of the disk in terms of Sigma0, rin and rout. Solve for 
    Sigma0 and plug back in...'''
    Mstar_cgs=Mstar*Msolar2g
    Mdisk_cgs=Mdisk*Msolar2g
    rout_cgs=rout*au2cm
    rin_cgs=rin*au2cm
    out=( (G*Mstar_cgs)**0.5 )*Mdisk_cgs*(2+beta)*((rout_cgs**(2.5+beta))-(rin_cgs**(2.5+beta)))\
        -Ltot*(2.5+beta)*( (rout_cgs**(2+beta))-(rin_cgs**(2+beta)) )
    #not too sure about the units....?
    return out

def rout_given_Mstar_Mdisk_Ltot(Mstar,Mdisk,Ltot,rin=0.005,beta=-1):
    #'''Given a keplerian disk of mass Mdisk with a powerlaw density profile
    #with index beta, around a star of Mstar calculate the outer radius given
    #the total angular momentum.
    #MATH STUFF: solve for Mdisk(r) assuming powerlaw density profile. rearrange
    #            to solve for Sigma_0, the normalization of the density profile
    #            as a function of r. Substitute this expression for Sigma_0 into
    #            the equation of Ltot(r), which itself is found by integrating and 
    #            includes a dependence on Sigma_0.
    #            rout 2pi
    #   Ldisk = S    S   Sigma(r)r(dtheta)(dr)(r**2)(GMstar/r)**0.5
    #            rin  0
    #***HOWEVER, THE EXPRESSION BELOW ASSUMES RIN=0!!!***
    #INPUTS:
    #Mdisk     -[float] the total initial mass of the disk in solar masses
    #Mstar     -[float] the mass of the central star in solar masses
    #Ltot      -[float] the total angular momentum of the disk in cgs
    #beta      -[optional,float] the power law index of the density profile
    #                            Sigma \propto r**beta
    #**Sigma0args - additional keywords to feed to Q.Sigma0 
    #RETURNS: rout in AU, optionally returns new Mstar and Mdisk...'''
    #Mdisk_cgs=Mdisk*Msolar2g
    #Mstar_cgs=Mstar*Msolar2g
    #rout=(1./(G*Mstar_cgs))*( (Ltot/Mdisk_cgs) * ((2.5+beta)/(2+beta)) )**2
    #return rout/au2cm
    func=lambda rout:rout_func(rout,Mstar=Mstar,Mdisk=Mdisk,Ltot=Ltot,rin=rin,beta=beta)
    rout=brentq(func,rin+rin*10e-6,1000)
    return rout

