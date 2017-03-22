__author__ = 'German - David'

class Estadisticas:
    def estadistica(self, cadena):
        if cadena == "":
            return 0
        elif cadena.count(",")== 1:
            return 2
        else:
            return 1
