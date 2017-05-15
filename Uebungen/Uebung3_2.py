import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

def f(x):
    return(float(5-float(x)/(1-np.exp(-float(x)))))
    
l=1
r=2

while f(l)*f(r)>0:
    l=l+1
    r=l+1

print('l=',l,' ','r=',r)

dx=0.000000000000001

while r>l+dx:
    m=(l+r)/2
    if f(m)*f(l)<0:
        r=m
    else:
        l=m

print(m)
