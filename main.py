import pygame
from pygame.constants import QUIT

import random

pygame.init()

print(random.random())

FPS = pygame.time.Clock()

HEIGHT = 400
WIDTH = 600

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_BLUE = (0, 0, 255)

flags = pygame.RESIZABLE
main_display =  pygame.display.set_mode((WIDTH, HEIGHT), flags)

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_BLUE)
player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

while playing:
   FPS.tick(240)
   for event in pygame.event.get():
      if event.type == QUIT:
         playing = False
    
   main_display.fill(COLOR_GREEN)

   if player_rect.bottom >= HEIGHT:
      player_speed[1]= -player_speed[1]
   
   if player_rect.right >= WIDTH: 
      player_speed[0] = -player_speed[0]

   if player_rect.top < 0:
      player_speed[1]= -player_speed[1]

   if player_rect.left <0:
      player_speed[0] = -player_speed[0]

   main_display.blit(player, player_rect)

   player_rect = player_rect.move(player_speed)
   
   pygame.display.flip()

pygame.quit()