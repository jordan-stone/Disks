import numpy as np
import matplotlib.pyplot as mpl
from Disks import *
from Disks.evolve import j_mdot_new_rout, Offner_McKee_dotm_2CTC, J0, J_of_m
from Disks.TvsR import active_and_irradiated_combined_opacity
from Disks import Q
from Disks.Baraffe import interpolate_baraffe

mf=0.08#star final mass
p_L=1.5#power-law index of angular momentum as a function of accreted mass.
j0=J0(p_L,mf,100)#units of specific angular momentum, 100 AU final radius...

mstar=[0.021]#first step star mass
mdot_star=[]
mdisk=[0.0002]#first step disk mass
routs=[10]#first step disk radius
tt=[0]#elapsed time
deltat=[0]
mdot_infs=[0]
Js=[]
Ltots=[]

oneMore=False
count=0

Qs=[]
scatter_qs=[]

while True:
    #infall a function of 1) current total, 2)final mass, 3) core Temp=50K.
    a_s=np.r_[0.006,np.linspace(0.05,routs[-1],100)]

    #below args are: accreted mass,final mass,envelope temperature in kelvin
    mdot_infs.append(Offner_McKee_dotm_2CTC(mstar[-1]+mdisk[-1],mf,50))

    #a 0 year old star with the given mass...This is probably defaulting...
    teff,radius=interpolate_baraffe(mstar[-1])
    print teff,radius

    TofR,MdotofR=active_and_irradiated_combined_opacity(a_s,
                                                        mstar[-1],
                                                        radius,
                                                        teff,
                                                        diskMassFrac=mdisk[-1]/mstar[-1],
                                                        amin=0.005,
                                                        aout=routs[-1],
                                                        sampled_ts=np.linspace(10,9999,100),
                                                        zero_find_default=teff)#get the accretion rate onto the star

    Qs.append(Q.Q(Q.cfromT(TofR),Q.Omega(mstar[-1],a_s),Q.Sigmar(mdisk[-1],a_s,beta=-1,rin=0.005,rout=routs[-1])))
    scatter_qs.extend(zip(map(lambda x: tt[-1],a_s),a_s,Qs[-1]))#tuples (time,radius,Q)

    mdot_star.append(MdotofR[0]*year2second/Msolar2g)

    deltat.append(0.05*(mdisk[-1]+mstar[-1])/max(mdot_infs[-1],mdot_star[-1]))

    Js.append(J_of_m((mstar[-1]+mdisk[-1]),mf,j0,p_L))#specific
    
    rout0,mstar0,mdisk0,Ltot0=j_mdot_new_rout(mstar[-1],mdisk[-1],
                                              mdot_star[-1],Js[-1],mdot_infs[-1],deltat[-1],
                                              rout_0=routs[-1],returnMstarMdisk=True)

    routs.append(rout0)
    mdisk.append(mdisk0)
    mstar.append(mstar0)
    Ltots.append(Ltot0)
    tt.append(tt[-1]+deltat[-1])
    #deltat.append((1/Q.Omega(mstar[-1],routs[-1]))/year2second)
    if oneMore:
        break
    if (mstar[-1]+mdisk[-1]) > mf:
        oneMore=True
    count+=1

from plottingTools.fixplotsImproved import compModern, tickFont
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter, MaxNLocator
f=mpl.figure(figsize=(16,8))
a=f.add_subplot(221)
a2=f.add_subplot(222)
a3=f.add_subplot(223)
a4=f.add_subplot(224)

#formatter=ScalarFormatter()
#formatter.set_powerlimits((-3,3))
#formatter.set_scientific(True)

a.loglog(t,routs,linewidth=3)
a.set_xlabel('Time [years]',fontproperties=compModern(25))
a.set_ylabel('R$_{\mathrm{out}}$ [AU]',fontproperties=compModern(25))
#formatter=FormatStrFormatter('%6.1e')
#locator=MaxNLocator(nbins=3,prune='both')
#a.xaxis.set_major_formatter(formatter)
#a.xaxis.set_major_locator(locator)
tickFont(a,'x',compModern(18))
tickFont(a,'y',compModern(18))

a2.loglog(t[1:],Ltots,linewidth=3)
a2.loglog(t[1:],np.cumsum(np.array(Js)*np.array(mdot_infs[1:])*Msolar2g*np.array(deltat[1:])),linewidth=3)
a2.set_xlabel('Time [years]',fontproperties=compModern(25))
a2.set_ylabel('L',fontproperties=compModern(25))
tickFont(a2,'x',compModern(18))
tickFont(a2,'y',compModern(18))

a3.loglog(t[1:],mdot_star,linewidth=3)
a3.set_xlabel('Time [years]',fontproperties=compModern(25))
a3.set_ylabel('$\dot{\mathrm{M}}_{*}$',fontproperties=compModern(25))
tickFont(a3,'x',compModern(18))
tickFont(a3,'y',compModern(18))

qplot=a4.scatter(map(lambda x:x[0],scatter_qs),map(lambda x:x[1],scatter_qs),c=map(lambda x:np.log10(x[2]),scatter_qs),lw=0)
a4.set_ylabel('radius')
a4.set_xlabel('time')
cbar=mpl.colorbar(qplot,orientation='horizontal')
cbar.set_label(r'log$_{10}$(Q)')

#mpl.tight_layout()
#mpl.tight_layout()
#mpl.tight_layout()
mpl.show()
mpl.show()
