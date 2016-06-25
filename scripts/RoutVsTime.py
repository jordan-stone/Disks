import numpy as np
import matplotlib.pyplot as mpl
from Disks import *
from Disks.evolve import j_mdot_new_rout, Offner_McKee_dotm_2CTC, J0, J_of_m
from Disks import Q

mf=0.05
j0=J0(1.5,mf,100)#units of specific angular momentum

mstar =[0.001]
mdisks=[0.0001]
routs=[0.5]
t=[0]
deltat=[0]
minfs=[0]
Js=[]
Ltots=[]

oneMore=False
while True:
    minfs.append(Offner_McKee_dotm_2CTC(mstar[-1]+mdisks[-1],mf,50))#m_current should be total star+disk mass
    mdot_star=minfs[-1]*0.9
    deltat.append(0.01*(mdisks[-1]+mstar[-1])/(minfs[-1]-mdot_star))
    Js.append(J_of_m((mstar[-1]+mdisks[-1]),mf,j0,1.5))#specific
    rout0,mstar0,mdisk0,Ltot0=j_mdot_new_rout(mstar[-1],mdisks[-1],
                                        mdot_star,Js[-1],minfs[-1],deltat[-1],
                                        rout_0=routs[-1],returnMstarMdisk=True)
    routs.append(rout0)
    mdisks.append(mdisk0)
    mstar.append(mstar0)
    Ltots.append(Ltot0)
    t.append(t[-1]+deltat[-1])
    #deltat.append((1/Q.Omega(mstar[-1],routs[-1]))/year2second)
    if oneMore:
        break
    if (mstar[-1]+mdisks[-1]) > mf:
        oneMore=True

from plottingTools.fixplotsImproved import compModern, tickFont
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter, MaxNLocator
f=mpl.figure(figsize=(16,8))
a=f.add_subplot(121)
a2=f.add_subplot(122)
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
a2.loglog(t[1:],np.cumsum(np.array(Js)*np.array(minfs[1:])*Msolar2g*np.array(deltat[1:])),linewidth=3)
a2.set_xlabel('Time [years]',fontproperties=compModern(25))
a2.set_ylabel('L',fontproperties=compModern(25))
tickFont(a2,'x',compModern(18))
tickFont(a2,'y',compModern(18))

mpl.tight_layout()
mpl.tight_layout()
mpl.tight_layout()
mpl.show()
mpl.show()
