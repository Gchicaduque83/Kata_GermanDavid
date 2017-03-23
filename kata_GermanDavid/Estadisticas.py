__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        numeros_vector = cadena.split(",")
        if cadena == "":
            return [0,0,0]
        else:
            minimo = int(min(cadena.split(",")))
        elementos = len(numeros_vector)
        return [elementos,minimo]


