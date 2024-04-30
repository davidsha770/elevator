import pygame
import sys
import random
from building import Building

# Initialize Pygame
pygame.init()


# Set up the display
height_screen = 700
width_screen = 1000
height_floor = 30
width_floor = 100
screen = pygame.display.set_mode((width_screen, height_screen))
clock = pygame.time.Clock()
pygame.display.set_caption("Building Floors")

street = []

for i in range(3):
    building = Building(10 + i * width_floor * 3 , random.randint(10, 20), 3, width_floor, height_floor, height_screen)
    street.append(building)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if left mouse button is pressed
            if event.button == 1:
                for building in street:
                    building.process_floor_click(pygame.mouse.get_pos())

    # Draw the floors
    screen.fill((255, 255, 255))  # Fill the screen with white
    for building in street:
        building.draw(screen)
        building.process_elevator_movement()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
