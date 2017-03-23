__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        numeros_vector = cadena.split(",")
        if cadena == "":
            return [0,0,0,0]
        elementos = len(numeros_vector)
        minimo = int(min(numeros_vector))
        maximo = int(max(numeros_vector))
        promedio = sum(int(vec) for vec in numeros_vector)/elementos
        return [elementos,minimo,maximo,promedio]


