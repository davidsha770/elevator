import pygame
from floor import Floor
from elevator import Elevator

class Building:
    def __init__(self, num_floors, num_elevators, floor_width, floor_height, height_screen):        
        self.last_time = pygame.time.get_ticks() / 1000 #in second
        self.num_floors = num_floors
        self.floor_width = floor_width
        self.floor_height = floor_height
        self.elevators = []
        for i in range(num_elevators):
            elv = Elevator(i, floor_height, floor_width/2 , height_screen, floor_width * (i/2 +1) + 10)
            self.elevators.append(elv)
        self.floors = []
        for i in range(num_floors+1):
            floor = Floor(i, 10, height_screen - (i + 1) * floor_height, floor_width, floor_height)
            self.floors.append(floor)

    def draw(self, surface):
        for floor in self.floors:
            floor.draw(surface)
        for elv in self.elevators:
            elv.draw(surface)

    def check_click(self, mouse_pos):
        for floor in self.floors:
            check = floor.check_click(mouse_pos)
            if check != -1:
                min_time = float('inf')
                min_elv = 0
                for elv in self.elevators:
                    time_elv = elv.calculate_time(check)
                    print(f"elv = {elv.number}, time = {time_elv}")
                    if time_elv < min_time:
                        min_time = time_elv
                        min_elv = elv.number

                time_to_add = abs(check - self.elevators[min_elv].target_floor)/2 + 2.0
                self.elevators[min_elv].add_to_queue(check)
                self.elevators[min_elv].add_time(time_to_add)
                return
            
            
    def manager(self):
        current_time = pygame.time.get_ticks() / 1000 #in second
        for elv in self.elevators:
            tarrget_floor = elv.target_floor
            height_floor = self.floors[tarrget_floor].get_rect().top
            floor = elv.manager(height_floor, current_time, self.last_time)
            if floor != -1:
                self.floors[floor].no_pressed()
        self.last_time = current_time
