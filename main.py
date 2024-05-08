import pygame
import sys
from configuration import load_config
from street import Street

def initialize_pygame(width_screen, height_screen):
    pygame.init()
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption("Building Floors")
    return screen

def draw_screen(screen, street):
    screen.fill((255, 255, 255))  # Fill the screen with white
    street.draw(screen)
    pygame.display.flip()

def main():
    height_screen, width_screen, buildings_info = load_config('configuration.txt')
    screen = initialize_pygame(width_screen, height_screen)
    street = Street(buildings_info, height_screen, width_screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        running = street.handle_events()
        draw_screen(screen, street)
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()