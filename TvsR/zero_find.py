import time
import numpy as np
import matplotlib.pyplot as mpl
from scipy.optimize import brentq

#def zero_find(func,x,default=10.):
#    posneg=(func(x)<0)
#    crossings=np.diff(posneg).nonzero()
#    if len(crossings[0])>1:
#        print 'more than one crossing found'
#    if len(crossings[0])<1:
#        print 'no crossing found, assuming minimum returning default'
#        mpl.plot(x,func(x))
#        raw_input()
#        return default
#    cross=crossings[0][0]
#    while True:
#        new_x=np.linspace(x[cross],x[cross+1],10)
#        posneg=(func(new_x)<0)
#        new_crossings=np.diff(posneg).nonzero()
#        if len(new_crossings)>1:
#            print 'more than one crossing found'
#        new_cross=new_crossings[0][0]
#        if np.abs(func(new_x[new_cross:new_cross+1]))<(1e-3):
#            #print np.abs(func(new_x[new_cross:new_cross+1])),'exiting##########################'
#            break
#        cross=new_cross
#        x=new_x
#    return new_x[new_cross]
#
def zero_find(func, x, default=10.):
    arr = np.array(map(func,x))
    posneg = (arr<0)
    crossings = np.diff(posneg).nonzero()
    if len(crossings[0]) > 1:
        print 'multiple zeros',x[crossings[0]],'using: ',x[crossings[0][0]]
        mpl.plot(x,arr,'r--')
        mpl.show()
    if len(crossings[0]) < 1:
        old_x = x
        for loop in xrange(4):
            new_x = np.linspace(np.min(old_x),np.max(old_x),2*len(old_x))
            arr=np.array(map(func,new_x))
            posneg=(arr<0)
            crossings=np.diff(posneg).nonzero()
            if len(crossings[0])>1:
                print 'multiple zeros',x[crossings[0]],'using: ',x[crossings[0][0]]
                x=new_x
                mpl.plot(x,arr,'r-')
                mpl.show()
                break
            if len(crossings[0])==1:
                x=new_x
                break
            old_x=new_x
        if len(crossings[0])<1:
            print 'no crossing found. returning default %f'%default
            outs=map(lambda t:func(t,returnTerms=True),old_x)
            exp=[o[0] for o in outs]
            term_1=[o[1] for o in outs]
            term_2=[o[2] for o in outs]
            term_3=[o[3] for o in outs]
            term_4=[o[4] for o in outs]
            mpl.figure()
            mpl.plot(old_x,exp,label='all')
            mpl.plot(old_x,term_1,label='t**4')
            mpl.plot(old_x,term_2,label='viscous1')
            mpl.plot(old_x,term_3,label='viscous2')
            mpl.plot(old_x,term_4,label='irr')
            mpl.legend()
            mpl.show()
            return default
    cross=crossings[0][0]
    #print 'crossing found!?'
    return brentq(func,x[cross],x[cross+1])
