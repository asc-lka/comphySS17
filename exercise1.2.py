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
	s = es+q**n
	 
print("Die Summe ändert sich für q = " + str(q) + " ab dem " + str(n-1) + ". Summanden nicht mehr und der Grenzwert lautet: " + str(s) + " und ist damit identisch mit dem wahren Grenzwert 1/(1-q)")

	
	
	
