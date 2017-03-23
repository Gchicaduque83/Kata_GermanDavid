__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        if cadena == "":
            return [0]
        else:
            elementos = len(cadena.split(","))
            return [elementos]


