from Disks import *
import numpy as np

def cfromT(T,mu=2.34):
    '''isothermal sound speed given temperature:
    inputs:
    T  - temperature in Kelvin
    mu - mean molecular weight of the gas in amu
    '''
    return (k_boltzmann*T/(amu2g*mu))**0.5
