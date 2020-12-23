def encuentra_palabra(archivo):

	filein = open(archivo, "r")
	texto = filein.readlines()

	nlines = len(texto)
	#print "hay {} linea en el texo".format(nlines)
	print "Esta es la ultima linea\n {}".format(texto[-1])
	linea = texto[-1]
	palabras = linea.split()	
        if "HAMLET" in linea:
		print "HAMLET esta en la linea"
	return palabras[0]

p = encuentra_palabra("hamlet.txt")
print "la palabra es: {}\n".format(p)
