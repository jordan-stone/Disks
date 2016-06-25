from Disks.evolve import *

def Offner_McKee_RMdot(T,Sigma_cl):
    '''This is Rmdot from Offner and McKee (2011) equation 14, which could be fed to 2CTC
    INPUTS:
    T in Kelvin
    Sigma_cl in g/cm**2
    RETURNS:
    unitless ratio...'''
    return (3.6e-5*Sigma_cl**0.75) / Offner_McKee_dotm_IS(T)
