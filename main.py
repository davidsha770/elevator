import pygame
import sys
import configparser
from street import Street

def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    
    height_screen = config.getint('Settings', 'height_screen')
    width_screen = config.getint('Settings', 'width_screen')
    
    buildings_info = []
    for key in config['Buildings']:
        floors, elevators = map(int, config['Buildings'][key].split(','))
        buildings_info.append([floors, elevators])
    
    return height_screen, width_screen, buildings_info

def initialize_pygame(width_screen, height_screen):
    pygame.init()
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption("Building Floors")
    return screen

def handle_events(street):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            street.handle_events(pygame.mouse.get_pos())
    return True

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
        running = handle_events(street)
        draw_screen(screen, street)
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()