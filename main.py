#Jona163
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

# Función para dibujar la simulación```python
def draw_simulation():
    # Limpiar la pantalla de simulación
    simulation_screen.fill(green)

    # Calcular la posición y la fuerza del amortiguador
    spring_force = -spring_stiffness * (player_rect.centery - height + spring_length)
    damping_force = -damping_factor * player_velocity
    total_force = spring_force + damping_force
    acceleration = total_force
    player_velocity += acceleration
    player_rect.centery += player_velocity


# Inicializar variables del juego principal
player_rect = car_image.get_rect(center=(250, 400))
vehicle_rects = []

# Parámetros del jugador y el vehículo
player_mass = 1.0

# Bucle del juego principal
while not gameover:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            gameover = True

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player_rect.move_ip(-100, 0)
            elif event.key == K_RIGHT:
                player_rect.move_ip(100, 0)

    # Limpiar la pantalla principal
    game_screen.fill(green)

    # Actualizar y dibujar el juego principal
    draw_game()
    screen.blit(game_screen, game_screen_rect)

    # Actualizar la pantalla principal
    pygame.display.update(game_screen_rect)

    # Salir del bucle si gameover es True
    if gameover:
        break

    # Añadir vehículos al juego
    if len(vehicle_rects) < 2:
        add_vehicle = True
        for vehicle_rect in vehicle_rects:
            if vehicle_rect[1].top < -100:
                add_vehicle = False
                break
        if add_vehicle:
            lane = random.choice([150, 250, 350])
            vehicle_images = [pickup_truck_image, semi_trailer_image, taxi_image, van_image]
            vehicle_image = random.choice(vehicle_images)
            vehicle_rects.append((vehicle_image, vehicle_image.get_rect(center=(lane, -100))))

    # Mover los vehículos y comprobar colisiones
    crash_rect = None
    for i, vehicle_rect in enumerate(vehicle_rects):
        vehicle_rect[1].move_ip(0, speed)
        if vehicle_rect[1].top > height:
            vehicle_rects.pop(i)
            score += 1
            if score % 5 == 0:
                speed += 1
                spring_stiffness += 0.05
                damping_factor += 0.05
        if vehicle_rect[1].colliderect(player_rect):
            gameover = True
            crash_rect = vehicle_rect[1]
            break

    # Actualizar la pantalla de simulación del amortiguador
    draw_simulation()
    screen.blit(simulation_screen, simulation_screen_rect)

    # Actualizar la pantalla de simulación del amortiguador
    pygame.display.update(simulation_screen_rect)

# Salir del juego
pygame.quit()
