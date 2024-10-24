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

# Función para dibujar el juego principal
def draw_game():
    # Dibujar la carretera
    game_screen.fill(green)
    pygame.draw.rect(game_screen, gray, (100, 0, 300, height))
    pygame.draw.rect(game_screen, yellow, (95, 0, 10, height))
    pygame.draw.rect(game_screen, yellow, (395, 0, 10, height))
    for y in range(-100, height + 100, 100):
        pygame.draw.rect(game_screen, white, (245, y, 10, 50))
    game_screen.blit(car_image, player_rect)

    # Mostrar la puntuación
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    game_screen.blit(text, text_rect)

    # Dibujar los vehículos
    for vehicle_rect in vehicle_rects:
        game_screen.blit(vehicle_rect[0], vehicle_rect[1])

    # Dibujar el choque si gameover es True
    if gameover:
        game_screen.blit(crash_image, crash_rect)
        pygame.draw.rect(game_screen, red, (0, 50, width // 2, 100))
        text = font.render('Modelado Terminado. ¿Deseas modelar de nuevo? (Presiona Y o N)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width // 4, 100)
        game_screen.blit(text, text_rect)
