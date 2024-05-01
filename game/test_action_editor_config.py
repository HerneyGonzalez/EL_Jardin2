import unittest
from ActionEditor_config import *

class TestActionEditorConfig(unittest.TestCase):
    def test_default_values(self):
        # Verificar los valores predeterminados de las propiedades
        self.assertEqual(default_transition, "dissolve")
        self.assertTrue(hide_window_in_animation)
        self.assertTrue(allow_animation_skip)
        self.assertEqual(default_warper, "linear")
        self.assertTrue(default_rot)

    def test_boolean_properties(self):
        # Verificar que las propiedades booleanas estén configuradas correctamente
        self.assertIsInstance(default_rot, bool)
        self.assertIsInstance(hide_window_in_animation, bool)
        self.assertIsInstance(allow_animation_skip, bool)
        self.assertIsInstance(default_rot, bool)
        self.assertIsInstance(fps_keymap, bool)
        self.assertIsInstance(default_show_camera_icon, bool)
        self.assertIsInstance(default_one_line_one_prop, bool)
        self.assertIsInstance(default_legacy_gui, bool)
        self.assertIsInstance(default_open_only_one_page, bool)
        self.assertIsInstance(default_sideview, bool)

    def test_wide_and_narrow_ranges(self):
        # Verificar los valores de las propiedades de rango amplio y estrecho
        self.assertEqual(wide_range, 1500)
        self.assertAlmostEqual(narrow_range, 7.0)
        self.assertAlmostEqual(narrow_drag_speed, 1./200)
        self.assertAlmostEqual(time_range, 7.0)
        self.assertEqual(tab_amount_in_page, 5)
        self.assertEqual(preview_size, 0.6)


    # Agrega más pruebas según sea necesario para cubrir otras propiedades y configuraciones...

if __name__ == '__main__':
    unittest.main()
