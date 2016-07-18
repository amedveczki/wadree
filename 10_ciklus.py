
# for VALTOZO in LISTA_VAGY_ITERABLE:
#    print VALTOZO
#
# a for belsejet annyiszor vegrehajtja, amennyi elem van LISTA -ban, vagy ITERABLE -ben
# VALTOZO pedig az egyes elemekre helyettesitodik be

kuttyok = ["Nyanc", "Torp", "Theo"]

for i in kuttyok:
	print (i*2)

# Ezt fogja kiirni:
# NyancNyanc
# TorpTorp
# TheoTheo
	
	
szamok = [100, 200, 300, 400]

for szam in szamok:
	print (szam)
	print (szam*2)
	
# Ezt fogja kiirni:
# 100
# 200
# 200
# 400
# 300
# 600
# 400
# 800
	
# range(darab)
# visszaad egy ITERABLE -t 0..darab-1 szamokat (osszesen darabot)

#for i in range(5):
#	print (i)
#
# ezt irja ki (tehat, osszesen 5 dbot):
# 0
# 1
# 2
# 3
# 4


# ures lista letrehozasa
x = []

try:
	db = int(input("Ird be hany elemet szeretnel: "))
except:
	print("Ez nem szam :(")
	exit() # ki lehet lepni vele

for i in range(db):
	# ezzel lesz ilyen stringunk: 0. szam:
	#                             1. szam:
	# ...stb, a str(i) az szovegge alakitja a szamot (mert range() szamokat ad vissza)
	szoveg = str(i) + ".szam: "
	
	# szoveg -et kiirjuk, es bekerjuk az elemet egyuttal
	uj_elem = input(szoveg)
	
	# x listahoz hozzaadjuk
	x.append(uj_elem)
	
print (x)


	


