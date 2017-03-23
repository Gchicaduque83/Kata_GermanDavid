from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_estadistica_elementos(self):
        self.assertEqual(Estadisticas().estadistica("")[0],0,"Cadena vacia")

    def test_estadistica_elemento1(self):
        cadena= "1"
        self.assertEqual(Estadisticas().estadistica(cadena)[0], len(cadena.split(",")),"Un numero")

    def  test_estadistica_elementos2(self):
        cadena= "1,2"
        self.assertEqual(Estadisticas().estadistica(cadena)[0], len(cadena.split(",")),"Dos numeros")

    def  test_estadistica_elementosN(self):
        cadena= "1,2,3,4,5,6,7,8,9"
        self.assertEqual(Estadisticas().estadistica(cadena)[0], len(cadena.split(",")),"N numeros")

    def test_estadistica_minimo(self):
        self.assertEqual(Estadisticas().estadistica("")[1], 0,"Cadena vacia")

    def test_estadistica_minimo1(self):
        cadena= "1"
        self.assertEqual(Estadisticas().estadistica(cadena)[1], int(cadena),"Un numero")

    def test_estadistica_minimo2(self):
        cadena= "2,1"
        self.assertEqual(Estadisticas().estadistica(cadena)[1], int(min(cadena.split(","))),"Dos numeros")

    def  test_estadistica_minimoN(self):
        cadena= "10,2,3,4,5,6,7,8,9"
        self.assertEqual(Estadisticas().estadistica(cadena)[1], int(min(cadena.split(","))),"N numeros")

    def test_estadistica_maximo(self):
        self.assertEqual(Estadisticas().estadistica("")[2], 0,"Cadena vacia")
