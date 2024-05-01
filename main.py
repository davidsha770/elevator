import pygame
import sys
import random
from factory import factory

height_screen = 700
width_screen = 1000
height_floor = 30
width_floor = 100
num_buildings = 3

def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((width_screen, height_screen))
    pygame.display.set_caption("Building Floors")
    return screen

def create_buildings():
    street = []
    for i in range(num_buildings):
        position = 10 + i * width_floor * 3
        floors = random.randint(10, 20)
        num_elevators = 3
        building = factory("building", position, floors, num_elevators, width_floor, height_floor, height_screen)
        street.append(building)
    return street

def handle_events(street):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for building in street:
                building.process_floor_click(pygame.mouse.get_pos())
    return True

def draw_screen(screen, street):
    screen.fill((255, 255, 255))  # Fill the screen with white
    for building in street:
        building.draw(screen)
        building.process_elevator_movement()
    pygame.display.flip()

def main():
    screen = initialize_pygame()
    street = create_buildings()
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events(street)
        draw_screen(screen, street)
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()