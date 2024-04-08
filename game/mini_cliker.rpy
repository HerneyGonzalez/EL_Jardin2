label mini_clicker:
init python:
    # Ventana de juego en el centro de la pantalla
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # Declaración automática de imágenes
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['images']
    # Efecto de destello
    flash = Fade(.25, 0, .5, color="#fff")
    flash2 = Fade(.25, 0, .5, color="#222")

# Configuración del juego:
    # Valor máximo de la barra
    max_points = 100
    # Nombre de la imagen (sin enumeración de cuadros)
    img_name = "n"
    # Primer y último cuadro de la animación
    minN = 1
    maxN = 14
    # Valor agregado a la barra al hacer clic
    # (Dificultad del juego: 2.0 - muy difícil, 3.0 - fácil)
    points_plus = 2.5

# Variables por defecto
    # Puedes cambiar este valor si deseas para ajustar el equilibrio del juego
    points_minus = 1.0
    # Tiempo permitido entre clics o velocidad de la animación (tiempo entre cambios de cuadro)
    ani_time = .1
    # Cuadro actual
    number = 0
    # Incremento de cuadro (+1/-1)
    plus = 1
    # Barra que debe llenarse
    points = 0
    # Clic reciente
    clicked = True
    # Cambiar cuadro de animación si hubo un clic reciente y redibujar la pantalla para ver los cambios
    def NextFrameF():
        global points, number, plus, clicked
        # Si hubo un clic reciente, continuamos con la animación, de lo contrario, no avanzamos al siguiente cuadro. Pausa
        if clicked:
            # Siguiente/anterior cuadro
            number += plus
            # Si excede el número de cuadros, la animación se invierte
            if number > maxN:
                number = maxN - 1
                plus = -plus
            if number < minN:
                number = minN + 1
                plus = -plus
        # Reducción de la barra si no ha habido clics recientes
        points -= points_minus
        if points < 0:
            points = 0
        clicked = False
        # Redibujar la pantalla
        renpy.restart_interaction()
    # Función → acción
    NextFrame = renpy.curry(NextFrameF)

# Pantalla de juego
screen clicker:
    # Modalidad verdadera para evitar que el juego continúe con clics del ratón
    modal True
    # Restablecer la configuración del juego al aparecer la pantalla
    on "show" action [SetVariable("number", 0), SetVariable("plus", 1), SetVariable("clicked", True)]
    # Cambiar el cuadro si ha habido un clic reciente y comprobar la derrota
    timer ani_time repeat True action [NextFrame(), If(points <= 0, true=Return(False), false=NullAction())]
    # Imagen con animación
    add img_name + str(number)
    # Mostrar un botón invisible para hacer clic
    # Al hacer clic, aumenta la barra y establece la bandera de clic
    button:
        text _(" ")
        xfill True
        yfill True
        background "#00000001"
        # Si la barra está llena, fin del juego, victoria
        action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, true=Return(True), false=NullAction())]
    # Clic alternativo con tecla de espacio
    key "K_SPACE" action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, true=Return(True), false=NullAction())]
    # Indicador
    vbar value StaticValue(points, max_points):
        align (0, 0) # Posición en la pantalla
        maximum (150, 150) # Tamaño
        left_bar "heartempty" # Corazón vacío
        right_bar "heart" # Corazón lleno
        thumb None # Aquí puedes poner un separador
        thumb_shadow None # Y la sombra

return
