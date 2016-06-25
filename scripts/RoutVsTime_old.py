import numpy as np
import matplotlib.pyplot as mpl
from Disks import *
from Disks.evolve import j_mdot_new_rout, Offner_McKee_dotm_2CTC
from Disks import Q
from Disks.TvsR.active_and_irradiated_semenov_opacity import active_and_irradiated_semenov_opacity
from plottingTools.fixplotsImproved import compModern, tickFont
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter, MaxNLocator


mdot_star=1e-9#eventually I need to be tied to TvsR, which will depend some path through Baraffe models
j=1e20
f=mpl.figure(figsize=(8,8))
a=f.add_subplot(221)
a2=f.add_subplot(222)
a3=f.add_subplot(223)
a4=f.add_subplot(224)
for mdot_star in (1e-9,1e-8,1e-7,1e-6):
    mf=0.05
    mstar =[0.001]
    mdisks=[0.0001]
    routs=[50.]
    t=[0]
    deltat=[0]
    minfs=[0]
    while (mstar[-1]+mdisks[-1]) < mf:
        dumT,dumMdot=active_and_irradiated_semenov_opacity(np.array([0.005,0.006]),mstar[-1],0.3,3000,diskMassFrac=mdisks[-1]/mstar[-1],aout=routs[-1],sampled_ts=np.linspace(500,3000,5000)
        mdot_star=dumMdot[0]
        mdot_inf=Offner_McKee_dotm_2CTC(mstar[-1]+mdisks[-1],mf,50)#m_current should be total star+disk mass
        minfs.append(mdot_inf)
        deltat.append(0.01*(mdisks[-1])/(minfs[-1]-mdot_star[-1]))
        rout0,mstar0,mdisk0=j_mdot_new_rout(mstar[-1],mdisks[-1],
                                            mdot_star[-1],j,mdot_inf,deltat[-1],
                                            rout_0=routs[-1],returnMstarMdisk=True)
        routs.append(rout0)
        mdisks.append(mdisk0)
        mstar.append(mstar0)
        t.append(t[-1]+deltat[-1])
        #deltat.append((1/Q.Omega(mstar[-1],routs[-1]))/year2second)


#formatter=ScalarFormatter()
#formatter.set_powerlimits((-3,3))
#formatter.set_scientific(True)

    a.loglog(t,routs,linewidth=3,label='%5.0e'%mdot_star)
    a.set_xlabel('Time [years]',fontproperties=compModern(25))
    a.set_ylabel('R$_{\mathrm{out}}$ [AU]',fontproperties=compModern(25))
    #formatter=FormatStrFormatter('%6.1e')
    #locator=MaxNLocator(nbins=3,prune='both')
    #a.xaxis.set_major_formatter(formatter)
    #a.xaxis.set_major_locator(locator)
    tickFont(a,'x',compModern(18))
    tickFont(a,'y',compModern(18))
    print len(t),len(mstar)
    a2.plot(t,mstar,linewidth=3,label='%5.0e'%mdot_star)
    a2.set_xlabel('Time [years]',fontproperties=compModern(25))
    a2.set_ylabel('M$_{*}$ [M$_{\odot}$]',fontproperties=compModern(25))
    a2.yaxis.get_major_formatter().set_powerlimits((-2,2))
    a2.xaxis.get_major_formatter().set_powerlimits((-2,2))
    #formatter=FormatStrFormatter('%6.1e')
    locator=MaxNLocator(nbins=4,prune='both')
    #a2.xaxis.set_major_formatter(formatter)
    a2.xaxis.set_major_locator(locator)
    tickFont(a2,'x',compModern(18))
    tickFont(a2,'y',compModern(18))
    a3.plot(t,mdisks,linewidth=3,label='%5.0e'%mdot_star)
    a3.plot(t,[s+d for s,d in zip(mstar,mdisks)],linewidth=3,color=a3.lines[-1].get_color(),linestyle='--')
    a3.yaxis.get_major_formatter().set_powerlimits((-2,2))
    a3.xaxis.get_major_formatter().set_powerlimits((-2,2))
    #formatter=FormatStrFormatter('%6.1e')
    locator=MaxNLocator(nbins=4,prune='both')
    #a3.xaxis.set_major_formatter(formatter)
    a3.xaxis.set_major_locator(locator)
    a3.set_xlabel('Time [years]',fontproperties=compModern(25))
    a3.set_ylabel('M$_{\mathrm{disk}}$ [M$_{\odot}$]',fontproperties=compModern(25))
    tickFont(a3,'x',compModern(18))
    tickFont(a3,'y',compModern(18))
    a4.plot(t,np.r_[minfs[1],minfs[1:]],linewidth=3,label='%5.0e'%mdot_star)
    a4.yaxis.get_major_formatter().set_powerlimits((-2,2))
    a4.xaxis.get_major_formatter().set_powerlimits((-2,2))
    #formatter=FormatStrFormatter('%6.1e')
    locator=MaxNLocator(nbins=4,prune='both')
    #a4.xaxis.set_major_formatter(formatter)
    a4.xaxis.set_major_locator(locator)
    locator=MaxNLocator(nbins=5)
    a4.yaxis.set_major_locator(locator)
    a4.set_xlabel('Time [years]',fontproperties=compModern(25))
    a4.set_ylabel('$\dot{\mathrm{M}}$[M$_{\odot}$/yr]',fontproperties=compModern(25))
    tickFont(a4,'x',compModern(18))
    tickFont(a4,'y',compModern(18))
a.legend(loc='upper left')

mpl.tight_layout()
mpl.tight_layout()
mpl.tight_layout()
mpl.show()
mpl.show()
