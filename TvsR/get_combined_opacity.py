import numpy as np
from SemenovOpacity import get_Semenov_opacity
from FergusonOpacity import get_Ferguson_opacity
import matplotlib.pyplot as mpl

def get_combined_opacity(T, density=10**-14, Rosseland=True):
    if T < 1000:
        return get_Semenov_opacity(T, density=density, Rosseland=Rosseland)
    elif T >= 1500:
        return get_Ferguson_opacity(T, density=density)
    else:
        f_frac=(((1/500.)*T) - 2.)
        s_frac=(((-1/500.)*T) + 3.)
        return f_frac*get_Ferguson_opacity(T,density=density) + s_frac*get_Semenov_opacity(T,density=density)

def make_combined(T, density=None):
    f_frac=(((1/500.)*T) - 2.)
    s_frac=(((-1/500.)*T) + 3.)
    return f_frac*get_Ferguson_opacity(T,density=density) + s_frac*get_Semenov_opacity(T,density=density)

def get_combined_opacity_array(T, density=10**-14, Rosseland=True):
    kappa=get_Semenov_opacity(T, density=density, Rosseland=Rosseland)
    Ferg_inds = T>1500
    kappa[Ferg_inds] = get_Ferguson_opacity(T[Ferg_inds], density=density)
    mid_inds = np.logical_and( T>1000, T<1500 )
    kappa[mid_inds] = make_combined(T[mid_inds], density=density)
    return kappa

