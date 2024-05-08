import pygame
import sys
from configuration import load_config
from street import Street

def main():
    height_screen, width_screen, buildings_info = load_config('configuration.txt')
    pygame.init()
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption("Building Floors")
    street = Street(buildings_info, height_screen, width_screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        running = street.handle_events()
        screen.fill((255, 255, 255))  # Fill the screen with white
        street.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()