import pygame
from pygame.locals import *
import time
import random

DEBUG = False
WIDTH = 480
HEIGHT = 640
RECT_SIZE = 10
UPADE_DELAY = 0.15

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
MY_UNIVERSAL_FONT = pygame.font.SysFont('Comic Sans MS', 30)

fruit_xy = [HEIGHT//2, WIDTH//2 + RECT_SIZE*3]
head_xy = [HEIGHT//2, WIDTH//2]
offset = [RECT_SIZE, 0]
body = [(-RECT_SIZE, 0)]

def calculate_offest(arr1:list, arr2:list, inverted = 0):
    if inverted: return [(arr1[0]-arr2[0])%HEIGHT, (arr1[1]-arr2[1])%WIDTH]
    return [(arr1[0]+arr2[0])%HEIGHT, (arr1[1]+arr2[1])%WIDTH]

running = True
last_update = time.time()
game_over_flag = False
previous_offset = offset
while running:
    #Input
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if (e.key==K_a or e.key==K_LEFT) and previous_offset != [RECT_SIZE, 0]: offset = [-RECT_SIZE, 0]
            if (e.key==K_d or e.key==K_RIGHT) and previous_offset != [-RECT_SIZE, 0]: offset = [RECT_SIZE, 0]
            if (e.key==K_w or e.key==K_UP) and previous_offset != [0, RECT_SIZE]: offset = [0, -RECT_SIZE]
            if (e.key==K_s or e.key==K_DOWN) and previous_offset != [0, -RECT_SIZE]: offset = [0, RECT_SIZE]
        
        if e.type == pygame.QUIT:
            running = False
    
    #Processing
    if last_update + UPADE_DELAY < time.time():
        head_xy = calculate_offest(head_xy, offset)
        body = [calculate_offest([0,0], offset, 1)] + body[:-1] # Updating body like FIFO
        previous_offset = offset
        last_update = time.time()
    
    #Graphics and cheking collision
    screen.fill((0,0,0))
    screen.blit(MY_UNIVERSAL_FONT.render("SCORE: "+str(len(body)).zfill(5), False, (255,255,255), (128, 0, 180)), (WIDTH-40, 40))
    pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect(head_xy, [RECT_SIZE, RECT_SIZE])) # Drawing head 
    if head_xy == fruit_xy:
        body = body + [body[0]]
    pointer = head_xy
    for part in body: # Drawing body
        pointer = calculate_offest(pointer, part)
        while pointer == fruit_xy or head_xy == fruit_xy:
            fruit_xy = [random.randint(0, (HEIGHT-1)//RECT_SIZE)*RECT_SIZE, random.randint(0, (WIDTH-1)//RECT_SIZE)*RECT_SIZE]
        if pointer == head_xy: # Game Over
            screen.blit(MY_UNIVERSAL_FONT.render("GAME OVER", False, (255,255,255), (255, 0, 0)), (HEIGHT//16, HEIGHT//16))
            running = False
            game_over_flag = True
        else: pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(pointer, [RECT_SIZE, RECT_SIZE]))
    pygame.draw.rect(screen, (0, 255, 0), pygame.rect.Rect(fruit_xy, [RECT_SIZE, RECT_SIZE]))
    if DEBUG:
        screen.blit(MY_UNIVERSAL_FONT.render(str(fruit_xy), False, (255,255,255), (255, 0, 0)), (100, 10))
    pygame.display.update()
    
while game_over_flag:
 for e in pygame.event.get():
  if e.type == pygame.QUIT:
   game_over_flag = False
pygame.quit()