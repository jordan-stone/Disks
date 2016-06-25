import numpy as np
import matplotlib.pyplot as mpl
from Disks import *
from Disks.evolve import j_mdot_new_rout, Offner_McKee_dotm_2CTC, J0, J_of_m,Rcirc
from Disks.TvsR import active_and_irradiated_combined_opacity
from Disks import Q
from Disks.Baraffe import interpolate_baraffe

mstar=0.02
mf=0.08#star final mass

j0_05=J0(0.5,mf,100)#units of specific angular momentum
j0_10=J0(1.0,mf,100)#units of specific angular momentum
j0_20=J0(2.0,mf,100)#units of specific angular momentum
j0_25=J0(2.5,mf,100)#units of specific angular momentum
j0_30=J0(3.0,mf,100)#units of specific angular momentum

Js_05=[]
Js_10=[]
Js_20=[]
Js_25=[]
Js_30=[]

Ltots=[]
routs_05=[]
routs_10=[]
routs_20=[]
routs_25=[]
routs_30=[]
t=[0]

oneMore=False
count=0
accreted_mass=0
while True:
    print
    minfs=(Offner_McKee_dotm_2CTC(mstar,mf,10))#infall a function of 1) current total, 2)final mass, 3) core Temp=50K.
    print 'MDOT INFALL:',minfs
    deltat=(0.05*(0.02)/minfs)

    Js_05.append(J_of_m((mstar+accreted_mass),mf,j0_05,0.5))#specific
    Js_10.append(J_of_m((mstar+accreted_mass),mf,j0_10,1.0))#specific
    Js_20.append(J_of_m((mstar+accreted_mass),mf,j0_20,2.0))#specific
    Js_25.append(J_of_m((mstar+accreted_mass),mf,j0_25,2.5))#specific
    Js_30.append(J_of_m((mstar+accreted_mass),mf,j0_30,3.0))#specific

    accreted_mass+=(minfs*deltat)

    routs_05.append(Rcirc(mstar,Js_05[-1]))
    routs_10.append(Rcirc(mstar,Js_10[-1]))
    routs_20.append(Rcirc(mstar,Js_20[-1]))
    routs_25.append(Rcirc(mstar,Js_25[-1]))
    routs_30.append(Rcirc(mstar,Js_30[-1]))


    t.append(t[-1]+deltat)

    if oneMore:
        break
    if (accreted_mass) > 0.06:
        oneMore=True
    count+=1

from plottingTools.fixplotsImproved import compModern, tickFont
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter, MaxNLocator
f=mpl.figure(figsize=(8,8))
a=f.add_subplot(111)

for r in (routs_05,
          routs_10,
          routs_20,
          routs_25,
          routs_30):
    a.loglog(t[:-1],r,linewidth=3)
a.set_xlabel('Time [years]',fontproperties=compModern(25))
a.set_ylabel('R$_{\mathrm{out}}$ [AU]',fontproperties=compModern(25))
tickFont(a,'x',compModern(18))
tickFont(a,'y',compModern(18))
mpl.tight_layout()
mpl.tight_layout()
mpl.tight_layout()
mpl.show()
mpl.show()
