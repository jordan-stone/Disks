from Disks.Baraffe import *
import numpy as np

sbc=5.670373e-5#cgs
Lsun2cgs=3.846e33#cgs
cm2Rsun=(1/6.955e10)

def R_from_T_and_L(T,Lsolar):
    Lcgs=Lsolar*Lsun2cgs
    return cm2Rsun*np.sqrt(Lcgs/(4*np.pi*sbc))/T**2
