import numpy as np
import matplotlib.pyplot as mpl
from Disks import *
from Disks.evolve import j_mdot_new_rout, Offner_McKee_dotm_2CTC, J0, J_of_m
from Disks.TvsR import active_and_irradiated_combined_opacity
from Disks import Q
from Disks.Baraffe import interpolate_baraffe

mf=0.08#star final mass
p_L=1.5
j0=J0(p_L,mf,100)#units of specific angular momentum

mstar=[0.02]#first step star mass
mdot_star=[]
mdisks=[0.002]#first step disk mass
routs=[20]#first step disk radius
t=[0]
deltat=[0]
minfs=[0]
Js=[]
Ltots=[]

oneMore=False
count=0
while count<200:
    Js.append(J_of_m((0.07),mf,j0,p_L))#some non-zero specific angular momentum, but should be times zero mass below..
    rout0,mstar0,mdisk0,Ltot0=j_mdot_new_rout(0.02,0.002,
                                              0,Js[-1],0,11000.,
                                              rout_0=routs[-1],rin=0.005,returnMstarMdisk=True)
    routs.append(rout0)
    Ltots.append(Ltot0)
    t.append(t[-1]+11000.)
    #deltat.append((1/Q.Omega(mstar[-1],routs[-1]))/year2second)
    count+=1

from plottingTools.fixplotsImproved import compModern, tickFont
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter, MaxNLocator
f=mpl.figure(figsize=(16,8))
a=f.add_subplot(211)
a2=f.add_subplot(212)
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
a2.set_xlabel('Time [years]',fontproperties=compModern(25))
a2.set_ylabel('L',fontproperties=compModern(25))
tickFont(a2,'x',compModern(18))
tickFont(a2,'y',compModern(18))

#a3.loglog(t[1:],mdot_star,linewidth=3)
#a3.set_xlabel('Time [years]',fontproperties=compModern(25))
#a3.set_ylabel('$\dot{\mathrm{M}}_{*}$',fontproperties=compModern(25))
#tickFont(a3,'x',compModern(18))
#tickFont(a3,'y',compModern(18))

mpl.tight_layout()
mpl.tight_layout()
mpl.tight_layout()
mpl.show()
mpl.show()
