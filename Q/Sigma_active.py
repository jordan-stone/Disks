from Disks import *
import numpy as np
from Disks.Q import *

def Sigma_active(Sigma,T,sigma_thresh=200.,T_thresh=800.):
    '''Return the MRI active surface density making very strong assumptions.
    First, wherever the disk is less dense than sigma_thresh, all the matter
    there is considered active. Next, wherever the disk is more dense than 
    sigma_thresh and cooler than T_thresh, we assume the existence of a dead
    zone and set the active portion of the disk to sigma thresh. Lastly, 
    Wherever the disk is hotter than T_thresh, we assume the whole disk is
    active. This formulation is based on the treatment by Martin et al. 2011.
    Inputs:
    Sigma        - the surface density in cgs
    T            - the temperature in K
    sigma_thresh - [optional default=200 g/cm^2], the threshold surface
                   density
    T_thresh     - [optional default=800 K], the threshold temperature.
    '''
    if Sigma<sigma_thresh:
        return Sigma
    elif Sigma>sigma_thresh and T>T_thresh:
        return Sigma
    else:
        return sigma_thresh

def Sigma_active_array(Sigma,T,sigma_thresh=200.,T_thresh=800.):
    '''Return the MRI active surface density making very strong assumptions.
    First, wherever the disk is less dense than sigma_thresh, all the matter
    there is considered active. Next, wherever the disk is more dense than 
    sigma_thresh and cooler than T_thresh, we assume the existence of a dead
    zone and set the active portion of the disk to sigma thresh. Lastly, 
    Wherever the disk is hotter than T_thresh, we assume the whole disk is
    active. This formulation is based on the treatment by Martin et al. 2011.
    Inputs:
    Sigma        - the surface density in cgs
    T            - the temperature in K
    sigma_thresh - [optional default=200 g/cm^2], the threshold surface
                   density
    T_thresh     - [optional default=800 K], the threshold temperature.
    '''
    T=np.array(T)
    Sigma=np.array(Sigma)
    Sigma=np.where(Sigma<sigma_thresh,Sigma,sigma_thresh)
    Sigma=np.where(np.logical_and(Sigma>sigma_thresh,T>T_thresh),Sigma,sigma_thresh)
    return Sigma
