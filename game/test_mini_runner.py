import unittest
from unittest.mock import MagicMock
import pygame
from mini_runner import FeedtheDragon, feed_the_dragon_screen, display_score, display_player_lives

class TestFeedtheDragon(unittest.TestCase):

    def setUp(self):
        self.dragon = FeedtheDragon()

    def test_initialization(self):
        self.assertIsNone(self.dragon.key_pressed)
        self.assertEqual(self.dragon.PLAYER_STARTING_LIVES, 5)
        # Agrega más pruebas de inicialización según sea necesario

    def test_player_movement(self):
        # Simula el evento de presionar la tecla hacia arriba
        self.dragon.event(MagicMock(type=pygame.KEYDOWN, key=pygame.K_UP), 0, 0, 0)
        self.assertEqual(self.dragon.key_pressed, "up")

        # Simula el evento de presionar la tecla hacia abajo
        self.dragon.event(MagicMock(type=pygame.KEYDOWN, key=pygame.K_DOWN), 0, 0, 0)
        self.assertEqual(self.dragon.key_pressed, "down")

        # Simula el evento de soltar la tecla
        self.dragon.event(MagicMock(type=pygame.KEYUP), 0, 0, 0)
        self.assertIsNone(self.dragon.key_pressed)

    # Agrega más pruebas para los otros métodos de la clase según sea necesario

class TestFeedtheDragonScreen(unittest.TestCase):

    def test_display_score(self):
        # Prueba de la función display_score
        score_text = display_score(0, 0)
        self.assertEqual(len(score_text), 5)
        # Agrega más pruebas según sea necesario

    def test_display_player_lives(self):
        # Prueba de la función display_player_lives
        lives_text = display_player_lives(0, 0)
        self.assertEqual(len(lives_text), 5)
        # Agrega más pruebas según sea necesario

    # Agrega más pruebas para otras funciones según sea necesario

if __name__ == '__main__':
    unittest.main()
