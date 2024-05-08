import pygame
from factory import factory

class Street:
    def __init__(self, buildings_info, height_screen, width_screen):
        self.buildings = []
        self.create_buildings(buildings_info, height_screen, width_screen)

    def create_buildings(self, buildings_info, height_screen, width_screen):
        sum_elevators = 0
        max_floor = 0
        for floors, elevators in buildings_info:
            sum_elevators += elevators / 2 + 1
            max_floor = max(max_floor, floors) + 1
        count = 0
        for floors, elevators in buildings_info:
            position = width_screen / sum_elevators * count + 10
            building = factory("building", position, floors, elevators, (width_screen - 20) / sum_elevators, (height_screen-10) / max_floor, height_screen)
            self.buildings.append(building)
            count += elevators / 2 + 1

    def draw(self, surface):
        for building in self.buildings:
            building.draw(surface)
            building.process_elevator_movement()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for building in self.buildings:
                    building.handle_events(pygame.mouse.get_pos())
        return True