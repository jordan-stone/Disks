from Disks.evolve import *
#from Disks.evolve.Offner_McKee_dotm_IS import Offner_McKee_dotm_IS

def Offner_McKee_dotm_2CTC(m_current,m_final,T_env,j=0.5,Rmdot=3.6):
    '''Offner and McKee (2011) Eq. 14, a model of accretion from a 
    two-component core. 
    INPUTS:
    m_current - the current total accreted mass in solar masses
    m_final   - the eventual final mass in solar masses
    T_env     - the temperature of the accreting envelope in Kelvin
    j         - a parameter which depends on the density profile McKee and Tan (2003) use 0.5
    Rmdot     - dotm_TC/dotm_IS
    RETURNS:
    dotm      - in solar masses per year
    '''
    m_is=Offner_McKee_dotm_IS(T_env)
    return m_is*( 1 + (Rmdot**2) * (m_current/m_final)**(2*j) * m_final**1.5 )**0.5
