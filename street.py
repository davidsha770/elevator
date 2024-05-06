from factory import factory

class Street:
    def __init__(self, buidings_info, height_screen, width_screen):
        self.buildings = []
        sum = 0
        max_floor = 0
        for i in buidings_info:
            sum += i[1]/2 + 1
            if i[0] > max_floor:
                max_floor = i[0]
        max_floor += 1
        count = 0
        for i in buidings_info:
            position = width_screen/sum * count + 10
            buiding = factory("building", position, i[0], i[1], (width_screen - 20)/sum, (height_screen-10)/max_floor, height_screen)
            self.buildings.append(buiding)
            count += i[1]/2 + 1

    def draw(self, surface):
        for building in self.buildings:
            building.draw(surface)
            building.process_elevator_movement()

    def handle_events(self, mouse_pos):
        for building in self.buildings:
            building.handle_events(mouse_pos)