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

# Cargar recursos de imagen
car_image = pygame.image.load('images/car.png')
pickup_truck_image = pygame.image.load('images/pickup_truck.png')
semi_trailer_image = pygame.image.load('images/semi_trailer.png')
taxi_image = pygame.image.load('images/taxi.png')
van_image = pygame.image.load('images/van.png')
crash_image = pygame.image.load('images/crash.png')

# Parámetros del amortiguador
spring_length = 200
spring_stiffness = 0.1
damping_factor = 0.2

# Inicializar variables del jugador
player_rect = car_image.get_rect(center=(250, 400))
player_velocity = 0
