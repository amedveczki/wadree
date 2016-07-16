# Írj egy programot, ami bekér egy egész számot. Ha páratlan, írja ki, hogy páratlan.
# Ha páros, akkor egy függvény segítségével szorozd meg kettővel, a függvény ezt adja vissza, és ezt a függvény hívása után
# (NEM a függvényben!) írd ki, azzal együtt, hogy páros.

# 40%: függvény nélkül, csak kíírja, hogy páros/páratlan
# 80%: függvénnyel, meg is duplázza
# 100%: a fentiek + hibakezelés

print ("Irj be egy tetszoleges egesz szamot!")

a = input()

def paratlan(a):
	return a % 2 == 1
		
def dupla(szam):
	return szam*2

try:
	a = int(a)
	if paratlan(a):
		print ("paratlan")	
	else: 
		print ("paros, a ketszerese:", dupla(a))

except:
	print ("Ez nem szam.")
		
	