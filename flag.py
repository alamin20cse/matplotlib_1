import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Waving Bangladesh Flag")

# Colors
GREEN = (0, 106, 78)   # Bangladesh flag green
RED = (244, 42, 65)    # Bangladesh flag red

# Clock for frame rate
clock = pygame.time.Clock()

def draw_flag(time):
    screen.fill((255, 255, 255))  # Background white

    # Draw waving green background
    flag_height = 200
    flag_width = 300
    top = 100
    left = 150
    wave_amplitude = 5
    wave_frequency = 0.05

    for y in range(flag_height):
        wave_offset = int(wave_amplitude * math.sin(wave_frequency * y + time))
        pygame.draw.line(screen, GREEN, (left + wave_offset, top + y), (left + flag_width + wave_offset, top + y))

    # Draw red circle (centered with slight waving)
    circle_radius = 40
    center_x = left + flag_width // 2 + int(wave_amplitude * math.sin(time + 2))
    center_y = top + flag_height // 2
    pygame.draw.circle(screen, RED, (center_x, center_y), circle_radius)

# Main loop
time = 0
running = True
while running:
    clock.tick(60)
    time += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_flag(time)
    pygame.display.flip()

pygame.quit()
sys.exit()
