import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

n = 1000000
gu=0
go=1
b=0.01

x=nr.random(n)
y=x**(2/3)

hist=[]

for i in range(int((go-gu)/b)):
    hist.append(0)
    
for i in range(n):
    k=int(y[i]*(go-gu)/0.01)
    hist[k]=hist[k]+1
    
xax = np.arange(0,1,0.01)
yax = 3/2*np.sqrt(xax)*1000000*0.01
plt.plot(xax,hist,'r')
plt.plot(xax,yax,'b')

plt.show()
    
    
