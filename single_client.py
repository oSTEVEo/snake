import pygame
from pygame.locals import *
import time
from vector import Vector2
from playground import Playgroud
from charater import Snake

pygame.init()
pygame.font.init() # needed?

UPADE_DELAY = 0.15
MENU_WIDTH = 640
MENU_HEIGHT = 480
RECT_SIZE = 10
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SALAD = (50, 200, 100)
GREEN = (0, 255, 0)
MAGNETA = (128, 0, 180)
BACKGROUND_COLOR = (0,0,0)
MENU_FONT = pygame.font.SysFont('Comic Sans MS', 30) # TODO centre

pg = Playgroud(MENU_HEIGHT//RECT_SIZE, MENU_WIDTH//RECT_SIZE)
snake_id = pg.add_player()
screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
game_status = 1
# 0 - main menu
# 1 - game
# [2,9] - reserved
# 10 - game over
heading = Vector2((1, 0))
prev_heading = heading
last_update = time.time()

# Main game loop
running = True
while running:
    # Draw menu
    if game_status == 0:
        screen.fill(BACKGROUND_COLOR)
        play_button_rect = screen.blit(MENU_FONT.render("PLAY", True, WHITE, RED), (MENU_WIDTH//2, MENU_HEIGHT//2))
        settings_button_rect = screen.blit(MENU_FONT.render("Settings (in progress)", True, WHITE, SALAD), (MENU_WIDTH//2, MENU_HEIGHT//2+40))

        # TODO
        # if play_button_rect.clicked == True:
        #    game_status == 1
        #    screen.fill(BACKGROUND_COLOR)

    # Input
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if (e.key==K_a or e.key==K_LEFT): heading = Vector2((-1,0))
            if (e.key==K_d or e.key==K_RIGHT): heading = Vector2((1,0))
            if (e.key==K_w or e.key==K_UP): heading = Vector2((0,-1))
            if (e.key==K_s or e.key==K_DOWN): heading = Vector2((0,1))
            if prev_heading == -heading: # to avoid dumb death
                heading = prev_heading

        if e.type == pygame.QUIT:
            running = False
    pg.snakes[snake_id].speed_vector = heading

    # Running
    if game_status:
        if last_update + UPADE_DELAY < time.time():
            pg.update()
            prev_heading = heading
            last_update = time.time()

        #render all
        screen.fill(BACKGROUND_COLOR)
        screen.blit(MENU_FONT.render("SCORE: "+str(pg.snakes[snake_id].score()).zfill(5), True, WHITE, MAGNETA), (MENU_WIDTH-100, 40))
        for snake in pg.snakes:
            if snake.status == 0: # skip dead snakes
                continue
            ptr = snake.head_pos
            pygame.draw.rect(screen, RED, pygame.rect.Rect((ptr*RECT_SIZE).coords(), [RECT_SIZE, RECT_SIZE]))
            for part in snake.body:
                ptr += part
                pygame.draw.rect(screen, WHITE, pygame.rect.Rect((ptr*RECT_SIZE).coords(), [RECT_SIZE, RECT_SIZE]))
        pygame.draw.rect(screen, GREEN, pygame.rect.Rect((pg.fruit_pos*RECT_SIZE).coords(), (RECT_SIZE, RECT_SIZE)))

    pygame.display.update()
pygame.quit()
