import pygame
import sys
from building import Building

# Initialize Pygame
pygame.init()


# Set up the display
height_screen = 700
width_screen = 400
screen = pygame.display.set_mode((width_screen, height_screen))
clock = pygame.time.Clock()
pygame.display.set_caption("Building Floors")

building = Building(22, 3, 100, 30, height_screen)

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
                building.process_floor_click(pygame.mouse.get_pos())

    # Draw the floors
    screen.fill((255, 255, 255))  # Fill the screen with white
    building.draw(screen)
    building.process_elevator_movement()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
