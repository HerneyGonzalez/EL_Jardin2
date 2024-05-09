label mini_finder:
    # define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]


    # El juego comienza aquí:
    label finddd:
        # Configuración del fondo, duración del juego en segundos,
        # y parámetros del juego: sprites y posiciones de los objetos a recolectar
        $ hf_init("bg room", 5,
            ("beer", 950, 705, _("Libro")),
            ("elf", 111, 660, _("Maquillaje")),
            ("flowers", 700, 370, _("Bolso")),
            ("skull", 1200, 880, _("Zapatos")),
            ("sprite", 1600, 550, _("Dinero")),
            # PARÁMETROS OPCIONALES:
            # Cambio de cursor al pasar el ratón
            mouse=True,
            # Inventario con eliminación de objetos encontrados
            inventory=False,
            # Mostrar pistas
            hint=True,
            # Resaltar objeto al pasar el cursor
            hover=brightness(.05),
            # Reducir el tamaño de las celdas del inventario para no interferir con la recolección
            w=200,
            h=200
        )

        # Mostrar fondo junto con los objetos y figuras en él
        $ hf_bg()
        with dissolve

        centered "{size=+24}"

        # Iniciar el juego
        $ hf_start()

        # Pausa dura para que el jugador deje de hacer clic y no se pierda los resultados
        $ renpy.pause(1, hard=True)

        # Resultados
        if hf_return == 0:
            centered "{size=+100}¡Ufff, a correr!"
        else:
            #define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]
            centered "{size=+100}¿Dónde está todo?\nMe faltaron [hf_return] cosas."
            jump mini_finder

        # Ocultar el juego
        $ hf_hide()
        with dissolve
        return
return
