__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        numeros_vector = cadena.split(",")
        if cadena == "":
            return [0,0]
        elif len(numeros_vector)==1:
            minimo = int(numeros_vector[0])
        else:
            if int(numeros_vector[0])<int(numeros_vector[1]):
                minimo = int(numeros_vector[0])
            else:
                minimo = int(numeros_vector[1])
        elementos = len(numeros_vector)
        return [elementos,minimo]


