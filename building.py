import pygame
from floor import Floor
from elevator import Elevator

class Building:
    def __init__(self, num_floors, floor_width, floor_height, height_screen):        
        self.last_time = pygame.time.get_ticks() / 1000 #in second
        self.num_floors = num_floors
        self.floor_width = floor_width
        self.floor_height = floor_height
        self.elv = Elevator(floor_height, floor_width/2 , height_screen, floor_width + 10)
        self.floors = []
        for i in range(num_floors+1):
            floor = Floor(i, 10, height_screen - (i + 1) * floor_height, floor_width, floor_height)
            self.floors.append(floor)

    def draw(self, surface):
        for floor in self.floors:
            floor.draw(surface)
        self.elv.draw(surface)

    def check_click(self, mouse_pos):
        for floor in self.floors:
            check = floor.check_click(mouse_pos)
            if check != -1:
                self.elv.add_to_queue(check)
                time_to_add = abs(check - self.elv.target_floor)/2 + 2.0
                self.elv.add_time(time_to_add)
                return
            
            
    def manager(self):
        current_time = pygame.time.get_ticks() / 1000 #in second
        tarrget_floor = self.elv.target_floor
        height_floor = self.floors[tarrget_floor].get_rect().top
        floor = self.elv.manager(height_floor, current_time, self.last_time)
        if floor != -1:
            self.floors[floor].no_pressed()
        self.last_time = current_time
