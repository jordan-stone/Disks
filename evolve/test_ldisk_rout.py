from rout_given_Mstar_Mdisk_Ltot import rout_given_Mstar_Mdisk_Ltot
from Ldisk_given_Mstar_Mdisk_rout import Ldisk_given_Mstar_Mdisk_rout

Lstart=Ldisk_given_Mstar_Mdisk_rout(0.08,0.008,rout=20,rin=0)
rstart=rout_given_Mstar_Mdisk_Ltot(0.08,0.008,Lstart)

print 'STARTS: '
print Lstart,rstart
Ls=[]
rs=[]
for ii in xrange(200):
    Lstart=Ldisk_given_Mstar_Mdisk_rout(0.08,0.008,rout=rstart,rin=0)
    rstart=rout_given_Mstar_Mdisk_Ltot(0.08,0.008,Lstart)
    Ls.append(Lstart)
    rs.append(rstart)
    print Lstart, rstart
