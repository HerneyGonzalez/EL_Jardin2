init python:

    # CONFIGURACIÓN DE JUEGO POR DEFECTO:

    # Conjunto de tipos de cartas por defecto
    all_cards = ['A', 'B', 'C']
    # Ancho y alto del tablero
    ww = 3
    hh = 3
    # Cantidad máxima de cartas que se pueden abrir en un solo turno
    max_c = 2
    # Tamaño del texto en las cartas en modo texto
    card_size = 48
    # Tiempo máximo para completar el juego
    max_time = 25
    # Pausa antes de que las cartas desaparezcan
    wait = 0.5
    # Modo de cartas con imágenes en lugar de texto
    img_mode = True

    values_list = []
    temp = []
    # Declaración de imágenes para las cartas
    # Deben estar en el formato "images/card_*.png"
    # Se requieren "card_back.png" y "card_empty.png"
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith((".png")):
            name = fn[12:-4]
            renpy.image("card " + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))
    # Si se encuentran más de 1 imagen,
    # cambiamos el conjunto de tipos de cartas, pero mantenemos los nombres de archivo
    if len(temp) > 1:
        all_cards = temp
    else:
        # En caso contrario, habilitamos el modo de texto,
        # ya que hay muy pocas imágenes
        img_mode = False

    # Función de inicialización del tablero de juego
    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

# Pantalla de juego
screen memo_scr:
    # Temporizador
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose")) repeat True
    # Tablero
    grid ww hh:
        align (.5, .5)  # En el centro
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card empty"
                    else:
                        text " " size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back"
                        else:
                            text "#" size card_size
                # Acción al hacer clic en la carta
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"])])
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

# Juego principal
label memoria_game:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range(0, len(values_list)):
            if values_list[i] == 'empty':
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": True})
            else:
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": False})
    $ memo_timer = max_time
    # Mostrar la pantalla de juego
    show screen memo_scr
    # Bucle principal del juego
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append(cards_list[result]["c_number"])
                $ turned_cards_values.append(cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # Evitar que se abran cartas adicionales
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause(wait, hard=True)
            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause(wait, hard=True)
            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump("memo_game_loop")
                renpy.jump("memo_game_win")
        jump memo_game_loop

# Derrota
label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause(0.1, hard=True)
    centered "{size=80}No quiero seguir pensando en el pasado{/size}"
    jump memoria_game

# Victoria
label memo_game_win:
    hide screen memo_scr
    $ renpy.pause(0.1, hard=True)
    centered "{size=80}{b}Al menos hay algunas cosas \n positivas entre mis recuerdos{/b}{/size}"
    return

# Ejemplo de inicio del juego
# label start:
    # scene black
    # $ max_time = 60
    # $ ww, hh = 4, 4
    # call memoria_game
    # return
