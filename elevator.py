import pygame
import queue

class Elevator:
    def __init__(self, height, width, height_screen, x):
        self.image = pygame.image.load("elv.png")
        self.image = pygame.transform.scale(self.image, (width ,height))
        self.ring = pygame.mixer.music.load("ding.mp3")
        self.floor = 0
        self.location = (x, height_screen - self.image.get_rect().height)
        self.target_floor = 0
        self.floor_height = height
        self.move_speed = 0.5  # Floors per second
        self.time_elapsed = 0
        self.q = queue.Queue()
        self.direction = "place"
        self.stay = False

    def draw(self, surface):
        surface.blit(self.image, self.location)

    def move(self, current_time, last_time, height_floor):
        distance_to_move = (current_time - last_time) * self.floor_height / self.move_speed
        if self.direction == "up" and self.location[1] > height_floor:
            self.location = (self.location[0], self.location[1] - distance_to_move)
        elif self.direction == "down" and self.location[1] < height_floor:
            self.location = (self.location[0], self.location[1] + distance_to_move)
        else:
            self.direction = "place"
            self.stay = True
            return 1
        return 0
    
    def stay_in_floor(self, current_time, last_time):
        self.time_elapsed += current_time - last_time
        if self.time_elapsed >= 2:
            self.stay = False
            self.time_elapsed = 0


    def manager(self, height_floor, current_time, last_time):
        if self.stay == True:
            self.stay_in_floor(current_time, last_time)
        elif self.direction != "place":
            if self.move(current_time, last_time, height_floor):
                pygame.mixer.music.play()
                return self.target_floor
        elif self.q.empty() == False:
            self.floor = self.target_floor
            self.target_floor = self.q.get()
            if self.floor < self.target_floor:
                self.direction = "up"
            else:
                self.direction = "down" 
        return -1
    
