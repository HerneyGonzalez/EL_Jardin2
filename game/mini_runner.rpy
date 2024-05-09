label mini_runner:

    init python:

        import random



        class FeedtheDragonDisplayable(renpy.Displayable):
            def __init__(self):
                renpy.Displayable.__init__(self)
                self.key_pressed = None # Esto almacenará la tecla presionada

                # Configura los valores del juego
                self.PLAYER_WIDTH = 250
                self.PLAYER_HEIGHT = 200
                self.COIN_WIDTH = 128
                self.COIN_HEIGHT = 128
                self.PLAYER_STARTING_LIVES = 5
                self.PLAYER_VELOCITY = 50
                self.COIN_STARTING_VELOCITY = 10
                self.COIN_ACCELERATION = 1
                self.BUFFER_DISTANCE = 100

                self.score = 0
                self.player_lives = self.PLAYER_STARTING_LIVES
                self.coin_velocity = self.COIN_STARTING_VELOCITY

                # Algunos elementos desplegables que utilizamos.
                self.player = Image("images/minigames/dragon_right.png")
                self.coin = Image("images/minigames/coin.png")

                # Posiciones de los dos elementos desplegables.
                self.px = 20
                self.py = 500
                self.pymin = 100
                self.pymax = 1080 - 256
                self.cx = 1920 + 128
                self.cy = random.randint(128, 1080 - 128)
                self.cymin = 100
                self.cymax = 1080 - 128

                # Tiempo del fotograma de renderizado anterior.
                self.oldst = None

                self.lose = False

                return

            # Dibuja la pantalla
            def render(self, width, height, st, at):

                # El objeto Render en el que dibujaremos.
                r = renpy.Render(width, height)

                # Calcula el tiempo transcurrido desde el fotograma anterior.
                if self.oldst is None:
                    self.oldst = st
                if self.key_pressed == "up":
                    self.py -= self.PLAYER_VELOCITY
                elif self.key_pressed == "down":
                    self.py += self.PLAYER_VELOCITY
                dtime = st - self.oldst
                self.oldst = st

                # Esto dibuja al jugador.
                def player(px, py, pymin, pymax):

                    # Dibuja la imagen del jugador.
                    player = renpy.render(self.player, width, height, st, at)

                    # renpy.render devuelve un objeto Render, que podemos
                    # blanquear en el objeto Render que estamos creando.
                    r.blit(player, (int(self.px), int(self.py)))
                
                # Esto dibuja la moneda.
                def coin(cx, cy, cymin, cymax):

                    # Dibuja la imagen de la moneda.
                    coin = renpy.render(self.coin, width, height, st, at)

                    # renpy.render devuelve un objeto Render, que podemos
                    # blanquear en el objeto Render que estamos creando.
                    r.blit(coin, (int(self.cx), int(self.cy)))

                if self.cx < -128:
                    # El jugador perdió la moneda
                    self.player_lives -= 1
                    renpy.sound.play("audio/minigames/miss_sound.ogg")
                    self.cx = width + 128
                    self.cy = random.randint(128, height - 128)
                else:
                    # Mueve la moneda
                    self.cx -= self.coin_velocity

                if self.py < self.pymin:
                    self.py = self.pymin               
                if self.py > self.pymax:
                    self.py = self.pymax

                if self.cy < self.cymin:
                    self.cy = self.cymin               
                if self.cy > self.cymax:
                    self.cy = self.cymax

                player(self.px, self.py, self.pymin, self.pymax)
                coin(self.cx, self.cy, self.cymin, self.cymax)

                # Comprueba colisiones
                def is_colliding(player, coin):
                    return (
                        self.px <= self.cx + self.COIN_WIDTH and
                        self.px + self.PLAYER_WIDTH >= self.cx and
                        self.py <= self.cy + self.COIN_HEIGHT and
                        self.py + self.PLAYER_HEIGHT >= self.cy
                    )
                
                if is_colliding(player, coin):
                    self.score += 1
                    renpy.sound.play("audio/minigames/coin_sound.ogg")
                    self.coin_velocity += self.COIN_ACCELERATION
                    self.cx = width + 128
                    self.cy = random.randint(128, height - 128)

                # Comprueba si perdió.
                if self.player_lives == 0:
                    self.lose = True

                    renpy.timeout(0)

                # Solicita que se vuelva a renderizar lo más pronto posible para mostrar el siguiente
                # fotograma.
                renpy.redraw(self, 0)

                # Devuelve el objeto Render.
                return r

            # Maneja los eventos.
            def event(self, ev, x, y, st):

                import pygame

                # Lo siguiente permite almacenar la tecla que se mantiene presionada.
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP and self.key_pressed != "up":
                    self.key_pressed = "up"
                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN and self.key_pressed != "down":
                    self.key_pressed = "down"
                elif ev.type == pygame.KEYUP:
                    self.key_pressed = None

                # Asegura que la pantalla se actualice.
                renpy.restart_interaction()

                # Si el jugador pierde, devuélvelo.
                if self.lose:
                    return self.lose
                else:
                    raise renpy.IgnoreEvent()

        def display_score(st, at):
            return Text(_("Flores: ") + "%d" % feed_the_dragon.score, size=40, color="#00cc00", outlines=[ (4, "#006600", 0, 0) ]), .1

        def display_player_lives(st, at):
            return Text(_("Vidas: ") + "%d" % feed_the_dragon.player_lives, size=40, color="#00cc00", outlines=[ (4, "#006600", 0, 0) ]), .1

        def move_up():
            feed_the_dragon.key_pressed = "up"

        def move_down():
            feed_the_dragon.key_pressed = "down"

        

    default feed_the_dragon = FeedtheDragonDisplayable()

    screen feed_the_dragon():

        add Solid("#272924")
        add Solid("#e6bb00", ysize=30, ypos=0.5)
        add Solid("#fff", ysize=15, ypos=0.9)
        add Solid("#fff", ysize=15, ypos=0.1)        

        add feed_the_dragon

        add DynamicDisplayable(display_score) xpos 240 xanchor 0.5 ypos 25

        add DynamicDisplayable(display_player_lives) xpos (1920 - 240) xanchor 0.5 ypos 25

        text _("Recoje flores de camino a Ibague"):
            xalign 0.5
            ypos 25
            size 40
            color "#00cc00"
            outlines [ (4, "#006600", 0, 0) ]
            #font "fonts\Mali\Mali-Bold.ttf"
        
        # Botón para mover hacia arriba
        imagebutton idle "images/up_button.png" action Function(move_up) xpos 50 ypos 185 

        # Botón para mover hacia abajo
        imagebutton idle "images/down_button.png" action Function(move_down) xpos 50 ypos 640
    label play_feed_the_dragon:

        #window hide  # Ocultar la ventana y el menú rápido mientras se juega a Feed the Dragon
        #$ quick_menu = False

        play music "audio/minigames/04.mp3"
        stop music
        $ feed_the_dragon.lose = False
        $ feed_the_dragon.score = 0
        $ feed_the_dragon.player_lives = 2
        $ feed_the_dragon.coin_velocity = feed_the_dragon.COIN_STARTING_VELOCITY
        $ feed_the_dragon.py = 500
        $ feed_the_dragon.cy = random.randint(128, 1080 - 128)

        call screen feed_the_dragon

        $ quick_menu = True
        window auto


return