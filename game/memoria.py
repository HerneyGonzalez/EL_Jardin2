# memoria.py

import random

# CONFIGURACIÓN DE JUEGO POR DEFECTO:

# Conjunto de tipos de cartas por defecto
all_cards = ['A', 'B', 'C']
# Ancho y alto del tablero
ww = 3
hh = 3
# Cantidad máxima de cartas que se pueden abrir en un solo turno
max_c = 2
# Tiempo máximo para completar el juego
max_time = 25
# Pausa antes de que las cartas desaparezcan
wait = 0.5
# Modo de cartas con imágenes en lugar de texto
img_mode = True

values_list = []

# Función de inicialización del tablero de juego
def cards_init():
    global values_list
    values_list = []
    while len(values_list) < ww * hh:
        current_card = random.choice(all_cards)
        values_list.append(current_card)
    random.shuffle(values_list)
    while len(values_list) < ww * hh:
        values_list.append('empty')




# Otras funciones del juego

# Aquí irían otras funciones relacionadas con el juego
