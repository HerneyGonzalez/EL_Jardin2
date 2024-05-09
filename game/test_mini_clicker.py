import unittest
from unittest.mock import patch
import mini_clicker_win  # Importar el módulo que contiene la función a probar

class TestMiniClicker(unittest.TestCase):
    @patch('builtins.print')  # Mockear la función print para no imprimir en consola durante las pruebas
    def test_mini_clicker_win(self, mock_print):
        # Simular entrada de datos
        mini_clicker_win._return = True
        mini_clicker_win.img_name = "image"
        mini_clicker_win.ani_time = 0.1

        # Llamar a la función que se está probando
        mini_clicker_win.mini_clicker_win()

        # Verificar que las llamadas a print fueron realizadas correctamente
        expected_calls = [
            'image0',  # Imagen inicial
            '',  # Texto vacío
            'image1', 'image2', 'image3', 'image4', 'image5', 'image5'  # Resultados del juego
        ]
        actual_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(actual_calls, expected_calls)

if __name__ == '__main__':
    unittest.main()
