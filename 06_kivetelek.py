try:
	print (sdff)
	print (19)
except:
	pass


print ("Irj be egy szamot!")

a = input()

try:
	# float() az lebegopontos
	x = int(a) * 2

	print ("A beirt szam ketszerese:", x)

except:
	print("Szamot, te idiota! Ez nem az, hanem:", a)