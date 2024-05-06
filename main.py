import pygame
import sys
from street import Street

height_screen = 700
width_screen = 1200
# buidings_info: the first is sum of floors, the second is sum of elevators
buidings_info = [[15, 3], [10, 2], [20, 4]]

def initialize_pygame():
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
    screen = initialize_pygame()
    street = Street(buidings_info, height_screen, width_screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events(street)
        draw_screen(screen, street)
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()