from Disks import *

def J0(p,mf,Rout):
    '''This is just a first try
    It assumes that the power-law index of the surface
    density profile is -1, and that the final disk mass is 0.1*Mf'''
    Rout_cgs=Rout*au2cm
    mf_cgs=mf*Msolar2g
    return (p+1)*(2./3.)*0.091*(Rout_cgs*G*mf_cgs/1.1)**0.5
