import os

# Función para establecer variables globales
def set_variable(var_name, value):
    globals()[var_name] = value

# Configuración de imágenes automáticas
config = {
    "automatic_images_minimum_components": 1,
    "automatic_images": [' ', '_', '/'],
    "automatic_images_strip": ['images']
}

# Clase para el efecto de destello
class Fade:
    def __init__(self, duration, start, end, color):
        self.duration = duration
        self.start = start
        self.end = end
        self.color = color

# Instancias de la clase Fade
flash = Fade(.25, 0, .5, color="#fff")
flash2 = Fade(.25, 0, .5, color="#222")

# Configuración del juego
max_points = 100  # Valor máximo de la barra
img_name = "n"  # Nombre de la imagen (sin enumeración de cuadros)
minN = 1  # Primer cuadro de la animación
maxN = 14  # Último cuadro de la animación
points_plus = 2.5  # Valor agregado a la barra al hacer clic (Dificultad del juego: 2.0 - muy difícil, 3.0 - fácil)

# Variables por defecto
points_minus = 1.0  # Puedes cambiar este valor si deseas para ajustar el equilibrio del juego
ani_time = .1  # Tiempo permitido entre clics o velocidad de la animación (tiempo entre cambios de cuadro)
number = 0  # Cuadro actual
plus = 1  # Incremento de cuadro (+1/-1)
points = 0  # Barra que debe llenarse
clicked = True  # Clic reciente

# Función para avanzar al siguiente cuadro y actualizar la barra
def NextFrameF():
    global points, number, plus, clicked

    if clicked:
        number += plus
        if number > maxN:
            number = maxN - 1
            plus = -plus
        if number < minN:
            number = minN + 1
            plus = -plus

    points -= points_minus
    if points < 0:
        points = 0
    clicked = False

# Configuración de la pantalla de juego
screen_clicker_config = {
    "on_show": [set_variable("number", 0), set_variable("plus", 1), set_variable("clicked", True)],
    "timer_ani_time": {
        "repeat": True,
        "action": [NextFrameF()]  # Aquí se debe ajustar la lógica según sea necesario
    }
}

# Clase para la pantalla de juego
class ScreenClicker:
    def __init__(self):
        self.config = screen_clicker_config

    def add_button(self):
        pass  # Implementación simulada

    def add_vbar(self):
        pass  # Implementación simulada

# Instancia de la pantalla de juego
screen_clicker = ScreenClicker()
screen_clicker.add_button()
screen_clicker.add_vbar()
