__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        numeros_vector = cadena.split(",")
        if cadena == "":
            return [0,0,0]
        else:
           maximo = int(max(numeros_vector))
        elementos = len(numeros_vector)
        minimo = int(min(numeros_vector))
        return [elementos,minimo, maximo]


