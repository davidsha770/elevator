# Main script to initialize and run the Pygame application
import pygame
import sys
from configuration import load_config
from street import Street

def main():
    # Load configuration settings from file
    height_screen, width_screen, buildings_info = load_config('configuration.txt')
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption("Building Floors")
    
    # Create a Street object with building information
    street = Street(buildings_info, height_screen, width_screen)
    
    # Clock object to manage frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        # Handle events and check if the program should continue running
        running = street.handle_events()
        
        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Draw the current state of the street
        street.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Maintain a frame rate of 60 frames per second
        clock.tick(60)

    # Quit Pygame and exit the program
    pygame.quit()
    sys.exit()

main()
