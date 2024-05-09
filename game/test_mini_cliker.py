#este es el test del juego del corazon
import unittest

# Aquí importa las clases y funciones que quieres probar
from mini_cliker import Fade, NextFrameF, ScreenClicker

class TestFade(unittest.TestCase):
    def test_init(self):
        fade = Fade(.25, 0, .5, color="#fff")
        self.assertEqual(fade.duration, .25)
        self.assertEqual(fade.start, 0)
        self.assertEqual(fade.end, .5)
        self.assertEqual(fade.color, "#fff")

class TestNextFrameF(unittest.TestCase):
    def test_NextFrameF(self):
        # Asegúrate de que los valores se actualicen correctamente
        global points, number, plus, clicked
        points = 10
        number = 5
        plus = 1
        clicked = True
        NextFrameF()
        self.assertEqual(points, 10)  # La barra se reduce en points_minus
        self.assertEqual(number, 5)  # El número del cuadro aumenta en plus

class TestScreenClicker(unittest.TestCase):
    def setUp(self):
        self.screen_clicker = ScreenClicker()

    def test_add_button(self):
        
        pass

    def test_add_vbar(self):
        
        pass

if __name__ == '__main__':
    unittest.main()
