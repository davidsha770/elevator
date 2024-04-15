from floor import Floor
from elevator import Elevator

class Building:
    def __init__(self, num_floors, floor_width, floor_height, height_screen):
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
                self.elv.q.put(check)
                return
            
            
    def manager(self):
        tarrget_floor = self.elv.target_floor
        height_floor = self.floors[tarrget_floor].rect.top
        floor = self.elv.manager(height_floor)
        if floor != -1:
            self.floors[floor].no_pressed()
