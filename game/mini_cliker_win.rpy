label mini_clicker_win:
    # Elementos innecesarios para la presentación
    scene expression (img_name + "0")
    pause .5
    show expression Text("") at truecenter as txt
    with dissolve
    pause
    hide txt
    # Comenzar con 10 puntos para no perder de inmediato
    $ points = 10

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
    call screen clicker # ←  juego
    # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑

    # Más elementos innecesarios a continuación:
    # Mostrar los resultados del juego
    if _return:
        # Retroceder la animación al último fotograma
        while number < maxN:
            $ number += 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + str(maxN))
        with flash
        show expression Text("") at truecenter as txt
    else:
        # Retroceder la animación al primer fotograma
        while number > 1:
            $ number -= 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + "0")
        with flash2
        show expression Text("") at truecenter as txt
    # Pausa dura en caso de que el jugador siga haciendo clic en el botón
    $ renpy.pause(1.0, hard=True)
    hide txt
    with dissolve
return

