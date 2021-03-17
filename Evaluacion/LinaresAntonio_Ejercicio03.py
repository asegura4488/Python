import random
def juega_datos(n_lanzamientos, n_dados, n_caras):
    merli = 0
    lista = []
    while merli < n_lanzamientos:
        
        cdados = 0
        conteo = 0
        
        aleatorios = {}
        while cdados < n_dados:
            aleatorios[cdados] = int((random.random()*100)) + 1
            cdados = cdados + 1
    
        while conteo < n_dados:
            ccaras = 1
            while ccaras <= n_caras:
                if aleatorios[conteo] <= int((ccaras/n_caras)*100):
                    aleatorios[conteo] = ccaras
                    break
                ccaras = ccaras+1
            conteo = conteo + 1
        
        cuenta = 0
        suma = 0
        while cuenta < (n_dados - 1):
            suma = suma + aleatorios[cuenta]
            cuenta = cuenta+1
            if cuenta == n_dados-1:
                suma = suma * aleatorios[cuenta]
        l = [suma]
        lista = lista + l
        merli = merli + 1

    return lista

