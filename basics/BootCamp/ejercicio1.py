f = open('texto.txt','r')

lineas = f.readlines()

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

conte = []
cuenta = 0

for i in range(len(alfabeto)):

    if not (cuenta == 0):
        conte.append(cuenta)
        cuenta = 0

    for k in range(len(lineas)):
        for j in range(len(lineas[k])):

            if(lineas[k][j] == alfabeto[i]):

                cuenta = cuenta + 1

f.close

e = open('conteo1.csv','w')

print(len(alfabeto), len(conte), "dfdf")

for i in range(len(alfabeto)):
    e.write('{},{},\n' .format(alfabeto[i], conte[i]))

e.close
