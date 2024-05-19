import pygame
import queue
from enum import Enum

# Enum to represent the direction of the elevator
class Direction(Enum):
    UP = "up"
    DOWN = "down"
    PLACE = "place"

class Elevator:
    def __init__(self, number, height, width, height_screen, x):
        # Load the elevator image and scale it to the appropriate size
        self.image = pygame.image.load("elv.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        
        # Load the sound for elevator arrival
        self.ring = pygame.mixer.music.load("ding.mp3")
        
        # Initialize elevator attributes
        self.number = number
        self.floor = 0
        self.location = (x, height_screen - self.image.get_rect().height)
        self.target_floor = 0
        self.floor_height = height
        self.elevator_speed = 0.5  # Floors per second
        self.time_elapsed = 0
        self.stay_time = 0
        self.queue = queue.Queue()
        self.last_floor = 0
        self.travel_direction = Direction.PLACE
        self.stay = False

    def draw(self, surface):
        # Draw the elevator at its current location
        surface.blit(self.image, self.location)

    def update_position(self, current_time, last_time, target_y):
        # Calculate the distance to move based on the time elapsed and elevator speed
        distance_to_move = (current_time - last_time) * self.floor_height / self.elevator_speed
        
        # Update the elevator's position based on its direction
        if self.travel_direction == Direction.UP and self.location[1] > target_y:
            self.location = (self.location[0], max(self.location[1] - distance_to_move, target_y))
        elif self.travel_direction == Direction.DOWN and self.location[1] < target_y:
            self.location = (self.location[0], min(self.location[1] + distance_to_move, target_y))
        else:
            # If the elevator has reached its target floor, stop moving
            self.travel_direction = Direction.PLACE
            self.stay = True
            return True
        return False

    def adjust_stay_time(self, current_time, last_time):
        # Adjust the stay time of the elevator when it reaches a floor
        self.stay_time += current_time - last_time
        if self.stay_time >= 2:
            self.stay = False
            self.stay_time = 0

    def process_movement(self, target_y, current_time, last_time):
        # Process the movement of the elevator
        if self.time_elapsed > 0:
            self.add_time(last_time - current_time)
        else:
            self.time_elapsed = 0
        
        if self.stay:
            # Adjust stay time if the elevator is staying at a floor
            self.adjust_stay_time(current_time, last_time)
        elif self.travel_direction != Direction.PLACE:
            # Update the position of the elevator if it is moving
            if self.update_position(current_time, last_time, target_y):
                pygame.mixer.music.play()  # Play the arrival sound
        elif not self.queue.empty():
            # Move to the next target floor in the queue
            self.floor = self.target_floor
            self.target_floor = self.queue.get()
            if self.floor < self.target_floor:
                self.travel_direction = Direction.UP
            else:
                self.travel_direction = Direction.DOWN

    def add_to_queue(self, floor):
        # Add a floor to the elevator's queue
        self.queue.put(floor)
        time_to_add = abs(floor - self.last_floor) * self.elevator_speed + 2
        self.last_floor = floor
        self.add_time(time_to_add)

    def add_time(self, time):
        # Add time to the elevator's elapsed time
        self.time_elapsed += time

    def calculate_time(self, floor):
        # Calculate the time it will take to reach a given floor
        return self.time_elapsed + abs(floor - self.last_floor) / 2

    def calculate_target_y(self, floor, height_screen):
        # Calculate the Y-coordinate for the center of the target floor
        return height_screen - (floor + 1) * self.floor_height
