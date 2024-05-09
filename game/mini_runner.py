import pygame
import random

class FeedtheDragon:
    def __init__(self):
        self.key_pressed = None
        
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
        
        self.player = pygame.image.load("C:/Users/equipo/Documents/GitHub/renpy-8.2.1-sdk/Desterrados_El_Jardin/game/images/minigames/dragon_right.png")
        self.coin = pygame.image.load("images/minigames/coin.png")
        
        self.px = 20
        self.py = 500
        self.pymin = 100
        self.pymax = 1080 - 256
        self.cx = 1920 + 128
        self.cy = random.randint(128, 1080 - 128)
        self.cymin = 100
        self.cymax = 1080 - 128
        
        self.oldst = None
        self.lose = False
        
    def render(self, width, height, st, at):
        r = pygame.Surface((width, height))
        
        if self.oldst is None:
            self.oldst = st
            
        if self.key_pressed == "up":
            self.py -= self.PLAYER_VELOCITY
        elif self.key_pressed == "down":
            self.py += self.PLAYER_VELOCITY
            
        dtime = st - self.oldst
        self.oldst = st
        
        if self.cx < -128:
            self.player_lives -= 1
            self.cx = width + 128
            self.cy = random.randint(128, height - 128)
            
        else:
            self.cx -= self.coin_velocity
            
        if self.py < self.pymin:
            self.py = self.pymin
            
        if self.py > self.pymax:
            self.py = self.pymax
            
        if self.cy < self.cymin:
            self.cy = self.cymin
            
        if self.cy > self.cymax:
            self.cy = self.cymax
            
        r.blit(self.player, (int(self.px), int(self.py)))
        r.blit(self.coin, (int(self.cx), int(self.cy)))
        
        if self.lose:
            pygame.time.wait(0)
            
        return r
    
    def event(self, ev, x, y, st):
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP and self.key_pressed != "up":
            self.key_pressed = "up"
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN and self.key_pressed != "down":
            self.key_pressed = "down"
        elif ev.type == pygame.KEYUP:
            self.key_pressed = None
            
        if self.lose:
            return self.lose

        return None

def display_score(st, at):
    return f"Mangos: {feed_the_dragon.score}", 40, (0, 204, 0), (4, (0, 102, 0), 0, 0), 0.1

def display_player_lives(st, at):
    return f"Vidas: {feed_the_dragon.player_lives}", 40, (0, 204, 0), (4, (0, 102, 0), 0, 0), 0.1

def move_up():
    feed_the_dragon.key_pressed = "up"

def move_down():
    feed_the_dragon.key_pressed = "down"

feed_the_dragon = FeedtheDragon()

def feed_the_dragon_screen():
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((39, 41, 36))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up()
                elif event.key == pygame.K_DOWN:
                    move_down()

        render_surface = feed_the_dragon.render(width, height, pygame.time.get_ticks(), 0)
        screen.blit(render_surface, (0, 0))

        score_text = display_score(pygame.time.get_ticks(), 0)
        screen.blit(*score_text, (240, 25))

        lives_text = display_player_lives(pygame.time.get_ticks(), 0)
        screen.blit(*lives_text, (1920 - 240, 25))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

feed_the_dragon_screen()
