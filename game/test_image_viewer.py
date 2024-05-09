import unittest
from unittest.mock import MagicMock, patch
import image_viewer_logic

class TestImageViewerFunctions(unittest.TestCase):
    
    def test_filter_image_name(self):
        # Caso de prueba 1: Verificar que filtre correctamente las imágenes
        # Definir un conjunto de imágenes simuladas
        image_viewer_logic.get_image_name_candidates = MagicMock(return_value=[("example_image", "example_image.png"), ("example_image", "example_image2.png")])
        filtered_list = image_viewer_logic.filter_image_name("example_image")
        # Extraer solo los nombres de archivo de la tupla
        filtered_list = [name[-1] for name in filtered_list]
        self.assertEqual(filtered_list, ["example_image.png", "example_image2.png"])

        # Caso de prueba 2: Verificar que filtre correctamente cuando no hay coincidencias
        image_viewer_logic.get_image_name_candidates = MagicMock(return_value=[])
        filtered_list = image_viewer_logic.filter_image_name("non_existing_image")
        self.assertEqual(filtered_list, [])
    
    def test_put_clipboard_text(self):
        # Simular el portapapeles
        scrap_mock = MagicMock()
        with patch('pygame.scrap', scrap_mock), \
             patch('image_viewer_logic.renpy.notify') as notify_mock:
            image_viewer_logic.put_clipboard_text("test_text")
            scrap_mock.put.assert_called_once_with(scrap_mock.locals.SCRAP_TEXT, b'test_text')
            notify_mock.assert_called_once_with("'test_text'\nis copied to clipboard")
if __name__ == '__main__':
    unittest.main()
