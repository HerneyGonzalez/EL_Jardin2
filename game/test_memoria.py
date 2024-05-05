# test_memoria.py

import unittest
from memoria import cards_init, values_list, ww, hh, max_c, all_cards

class TestMemoria(unittest.TestCase):

    def test_cards_init(self):
        # Llama a la función cards_init() para inicializar las cartas
        cards_init()

        # Reimporta las variables después de llamar a cards_init()
        from memoria import values_list, ww, hh, max_c

        # Verifica que la cantidad de cartas inicializadas sea la esperada
        self.assertEqual(len(values_list), ww * hh, "La cantidad de cartas inicializadas no es correcta")
        # Verifica que todas las cartas estén en el conjunto all_cards
        self.assertTrue(all(card in all_cards for card in values_list), "No todas las cartas son del conjunto all_cards")


    def test_game_loop(self):
    # Simula el bucle principal del juego
    # Nota: Esta es una simulación básica y no cubre todas las posibles ramas del código

    # Llama a la función cards_init() para inicializar las cartas
        cards_init()

    # Simula el comportamiento del juego
        can_click = True
        turned_cards_numbers = []
        turned_cards_values = []
        turns_left = max_c

    # Simula el bucle de turnos del juego
        while turns_left > 0 and len(values_list) > 0:  # Añadimos len(values_list) > 0 para asegurarnos de que aún hay cartas en el juego
            # Simula la selección de una carta
            selected_card_number = 0  # Selecciona la primera carta en este ejemplo
            if selected_card_number < len(values_list):  # Añadimos esta comprobación para evitar el IndexError
                selected_card_value = values_list[selected_card_number]

                # Registra la carta seleccionada
                turned_cards_numbers.append(selected_card_number)
                turned_cards_values.append(selected_card_value)

                # Simula la reducción de turnos
                turns_left -= 1

        # Verifica que el número de cartas volteadas sea el esperado
        self.assertEqual(len(turned_cards_numbers), min(len(values_list), max_c), "El número de cartas volteadas no es correcto")

        # Verifica que todas las cartas volteadas sean distintas
        self.assertEqual(len(set(turned_cards_values)), min(len(values_list), max_c), "No todas las cartas volteadas son distintas")


if __name__ == '__main__':
    unittest.main()
