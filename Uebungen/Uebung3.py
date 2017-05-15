import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

n=100000

aa=nr.random(n)
a=aa*2-1

t=np.arccos(a)

ff=nr.random(n)
f=ff*2*np.pi

kx=np.sin(t)*np.cos(f)
ky=np.sin(t)*np.sin(f)
kz=np.cos(t)

b=np.pi/2-t
l=np.empty(0)

for ef in f:
    if ef <= np.pi:
        l=np.append(l,ef)
    else:
        l=np.append(l,-np.pi+(ef-np.pi))


#print(l)

x=2*np.sqrt(2)*np.cos(b)*np.sin(l/2)/np.sqrt(1+np.cos(b)*np.cos(l/2))
y=np.sqrt(2)*np.sin(b)/np.sqrt(1+np.cos(b)*np.cos(l/2))

plt.plot(x,y,'b,')
plt.axis('equal')

plt.show()
