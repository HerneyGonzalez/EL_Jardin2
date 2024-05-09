import time

def mini_clicker_win():
    # Mostrar imagen inicial
    print(img_name + "0")
    time.sleep(0.5)

    # Mostrar texto vacío en el centro de la pantalla
    print("")

    # Comenzar con 10 puntos
    points = 10

    # Llamar a la función del juego (simulada)
    clicker_game()

    # Mostrar resultados del juego
    if _return:
        # Retroceder la animación al último fotograma
        number = 0
        maxN = 5  # Se debe definir el valor de maxN
        while number < maxN:
            number += 1
            print(img_name + str(number))
            time.sleep(ani_time)
        print(img_name + str(maxN))
    else:
        # Retroceder la animación al primer fotograma
        number = maxN
        while number > 0:
            number -= 1
            print(img_name + str(number))
            time.sleep(ani_time)
        print(img_name + "0")

    # Pausa en caso de que el jugador siga haciendo clic
    time.sleep(1.0)

def clicker_game():
    # Aquí iría la lógica del juego
    pass

# Llamada a la función principal
if __name__ == "__main__":
    _return = False
    img_name = "image"
    ani_time = 0.1
    mini_clicker_win()
