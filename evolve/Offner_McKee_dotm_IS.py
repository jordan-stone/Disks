def Offner_McKee_dotm_IS(T):
    '''Offner and McKee (2011) Eq. 6, from Shu 77
    INPUT:
    T in Kelvin
    RETURNS:
    mdot in solar masses per year'''
    return (1.54e-6)*(T/10.)**1.5
