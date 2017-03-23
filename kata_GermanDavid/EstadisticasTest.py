from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_estadistica(self):
        self.assertEqual(Estadisticas().estadistica(""),[0],"Cadena vacia")

    def test_estadistica1(self):
        cadena= "1"
        self.assertEqual(Estadisticas().estadistica(cadena)[0], len(cadena.split(",")),"Un numero")

    def  test_estadistica2(self):
        cadena= "1,2"
        self.assertEqual(Estadisticas().estadistica(cadena)[0], len(cadena.split(",")),"Dos numeros")

    def  test_estadisticaN(self):
        cadena= "1,2,3,4,5,6,7,8,9"
        self.assertEqual(Estadisticas().estadistica(cadena)[0], len(cadena.split(",")),"N numeros")

