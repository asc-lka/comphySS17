e = 1.0
n = 0

while 1+e/2 > 1:
	e = e/2
	n = n+1

typ_e = type(1+e/2)
	
print("Die überprüfte Zahl ist ein " + str(typ_e) + ".")
print("Es gibt keinen Unterschied mehr bei 1/(2^" + str(n) + ") , was ungefähr " + str(e) + " entspricht.")

	
	
	
