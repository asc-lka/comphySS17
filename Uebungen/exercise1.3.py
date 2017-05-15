import math

# Wir wollen ein Polynom  a_i * x**i from 0 to n, wobei n der Grad des Polynoms ist, in die Form des Horner-Schemas bringen: p(x) = x*(...(a_{n-2}+x*(a_n * x + a_{n-1}))) .

g=input("Um ein Polynom der Form p(x) = a_n * x^n + ... + a_0 ins Horner-Schema p(x) = x*(...(a_{n-2}+x*(a_n * x + a_{n-1}))) zu transferieren, werden Sie jetzt nach den Koeffizienten Ihres Polynoms gefragt. Tippen Sie bitte zunächst den Grad ihres Polynoms ein. \n")

g=int(g)

#print("Echo: " + str(g))

a_0=input("Wie lautet der Koeffizient des Summanden, der kein x beinhaltet? \n")

l=[0]*(g+1)

l[0]=a_0

#print(l)

#length=len(l)

#print(length)

for i in range(g+1):
    if i!=0:
        l[i]=input("Wie lautet der Koeffizient, der vor x^" + str(i) + " steht? \n")
       
p="p(x)="
k = ""

for i in range(g):
    p=p + str(l[i]) + "+x*("
    k=k + ")"
    
p=p + str(l[g]) + k

p = p.replace("0+","")

                 

print(p)
    
