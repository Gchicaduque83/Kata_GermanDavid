__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        numeros_vector = cadena.split(",")
        if cadena == "":
            return [0,0,0,0]
        elif len(numeros_vector) == 1:
           promedio = numeros_vector[0]
        else:
           promedio = (int(numeros_vector[0])+int(numeros_vector[1]))/2
        elementos = len(numeros_vector)
        minimo = int(min(numeros_vector))
        maximo = int(max(numeros_vector))
        return [elementos,minimo,maximo,promedio]


