q = input("Tippen Sie die Zahl ein, die sie für q wählen wollen. \n")
q=float(q)
n=0
n=int(n)
s=1
s=float(s)
es = 0
es = float(es)


while s > es:
    es = s
    n = n+1
    s = 1 + q * es
    
print("Berechnet man die Partialsummen mit dem Horner-Schema, so ändert sich die Summe für q = " + str(q) + " ab dem " + str(n-1) + ". Summanden nicht mehr und der Grenzwert lautet: " + str(s) + " und ist damit ebenso identisch mit dem wahren Grenzwert 1/(1-q) \n")	
	
def f(o):
    if(o < 1 + q * o):
        return f(1 + q * o)
    else:
        return o
        
print("Grenzwert mit Rekursion: " + str(f(0)))

