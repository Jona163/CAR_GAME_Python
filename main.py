import pygame
from pygame.locals import *
import random

pygame.init()

# Creación de la ventana
width = 800
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('MODELADO')

# Colores de la zona
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# Ajustes del stteo
clock = pygame.time.Clock()
fps = 120

# Ajustes del juego principal
gameover = False
speed = 2
score = 0
# Posiciones y tamaños de las pantallas
game_screen_rect = pygame.Rect(0, 0, width // 2, height)
simulation_screen_rect = pygame.Rect(width // 2, 0, width // 2, height)

# Inicializar superficies para las pantallas
game_screen = pygame.Surface(game_screen_rect.size)
simulation_screen = pygame.Surface(simulation_screen_rect.size)
