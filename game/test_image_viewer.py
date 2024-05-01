import unittest
from image_viewer_logic import filter_image_name, put_clipboard_text, tag_completion, _image_viewer_hide, ShowImage, Add_tag_or_Return

class TestImageViewerFunctions(unittest.TestCase):
    
    def test_filter_image_name(self):
        # Caso de prueba 1: Verificar que filtre correctamente las imágenes
        filtered_list = filter_image_name("example_image")
        self.assertEqual(filtered_list, ["example_image.png", "example_image2.png"])

        # Caso de prueba 2: Verificar que filtre correctamente cuando no hay coincidencias
        filtered_list = filter_image_name("non_existing_image")
        self.assertEqual(filtered_list, [])

        # Agrega más casos de prueba según sea necesario
    
    def test_put_clipboard_text(self):
        # Simular el portapapeles
        class MockScrap:
            @staticmethod
            def put(*args, **kwargs):
                return True

        # Sobrescribe la función scrap.put con nuestro MockScrap
        put_clipboard_text("test_text")
        # Aquí deberías agregar una aserción que verifique si el texto "test_text" está en el portapapeles

    # Agrega más pruebas para ShowImage y Add_tag_or_Return según sea necesario

if __name__ == '__main__':
    unittest.main()
