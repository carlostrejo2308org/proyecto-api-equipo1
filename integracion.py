from turtle import bk
import unittest
import tkinter as ktr
from Interfaz import VentanaId as Itr
from book import Book as Bk

class Test_Integracion(unittest.TestCase):
    def test_InterfazBusqueda(self):
        root = ktr.Tk()
        entrada = Itr(root) # Modulo Interfaz
        salida = Bk() #Modulo Libro
        casos = [
            (entrada.buscar("UpNHAQAAMAAJ"), salida.ExtraerElementos("UpNHAQAAMAAJ")),
            (entrada.buscar("DgbhAAAAMAAJ"), salida.ExtraerElementos("DgbhAAAAMAAJ")),
            (entrada.buscar("gqDf__ULmR8C"), salida.ExtraerElementos("gqDf__ULmR8C")),
        ]
        
        for inp, expected in casos:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(inp, expected, "(%s) deberia ser %s" % (inp, expected))

if __name__ == "__main__":
    unittest.main()
