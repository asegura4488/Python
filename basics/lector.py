filein = open("hamlet.txt", "r")
texto = filein.readlines()

nlines = len(texto)
print "hay {} linea en el texo".format(nlines)
print "Esta es la ultima linea\n {}".format(texto[-1])
linea = texto[-1]
palabras = linea.split()
print palabras
