from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_estadistica(self):
        self.assertEqual(Estadisticas().estadistica(""),0,"Cadena vacia")

    def test_estadistica1(self):
        self.assertEqual(Estadisticas().estadistica("5"),1,"Un numero")

    def  test_estadistica2(self):
        self.assertEqual(Estadisticas().estadistica("1,2"),2,"Dos numeros")

    def  test_estadisticaN(self):
        self.assertEqual(Estadisticas().estadistica("1,2,3"),3,"N numeros")