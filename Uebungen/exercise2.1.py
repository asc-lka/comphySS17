import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

n=500000

ls=nr.random(n)
lt=nr.random(n)


lr=[]
for x in ls:
    lr.append(np.sqrt(-2*np.log(x)))
        
lp=[]
for i in lt:
    lp.append(2*np.pi*i)

#print(lr)
#print(lp)

lx1=[]
lx2=[]
for i in range(n):
    lx1.append(-5.6+2.5*lr[i]*np.cos(lp[i]))
    lx2.append(-5.6+2.5*lr[i]*np.sin(lp[i]))
    
lx=lx1+lx2

#print(lx)
    
hist=[]

for i in range(int(20/0.01)):
    hist.append(0)
    
for i in range(2*n):
    if float(lx[i])>=-15 and float(lx[i])<5:
        k=int((lx[i]+15)/0.01)
        hist[k]=hist[k]+1
        
#print(hist)

#number = int(0)
#for i in range(2000):
#    number=number+hist[i]
    
#print(number)

#m=-15
#a=[]

#for i in range(2000):
#    m=m+0.01
#    a.append(m)
    
#print(a)

xax = np.arange(-15,5,0.01)
yax = 1/np.sqrt(2*np.pi*2.5**2)*np.exp(-(xax+5.6)**2/2/2.5**2)*1000000*0.01
plt.plot(xax,hist,'r')
plt.plot(xax,yax,'b')

plt.show()



    

    
    
