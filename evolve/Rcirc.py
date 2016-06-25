from Disks import *

def Rcirc(Mstar,j):
    '''Given a central mass of Mstar, return
    the radius at which material with specific angular
    momentum j will circularize.
    INPUTS:
    Mstar - the central mass in Msol
    j     - the specific angular momentum in cgs
    RETURNS:
    Rcirc - the circularization radius in AU'''
    return ((j**2)/(G*Mstar*Msolar2g))/au2cm

