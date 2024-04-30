import pygame

class Floor:
    def __init__(self, number, x, y, width, height):
        self.number = number
        self.press = False
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (192, 192, 192)
        self.brick_color = (255, 0, 0)
        self.black_line_color = (0, 0, 0)
        self.height_black_line = 4
        self.font = pygame.font.SysFont(None, 24)
        self.number_color = (0, 0, 0)
        self.time = 0

    def draw(self, surface):
        self.draw_floor(surface)
        self.draw_number(surface)
        if self.time > 0:
            self.draw_timer(surface)

    def draw_floor(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        brick_width = 4
        brick_height = 2
        # Draw bricks pattern with spacing between bricks
        spacing = 1
        i = 0
        for row in range(0, self.rect.height - brick_height, brick_height + spacing):
            if i % 2:
                for col in range(0, self.rect.width - brick_width, brick_width + spacing):
                    brick_rect = pygame.Rect(self.rect.left + col, self.rect.top + row, brick_width, brick_height)
                    pygame.draw.rect(surface, self.brick_color, brick_rect)
            else:
                for col in range(int(brick_width / 2), self.rect.width - brick_width, brick_width + spacing):
                    brick_rect = pygame.Rect(self.rect.left + col, self.rect.top + row, brick_width, brick_height)
                    pygame.draw.rect(surface, self.brick_color, brick_rect)
            i += 1

        # Draw black line at the bottom
        pygame.draw.rect(surface, self.black_line_color, (self.rect.left,\
                                                        self.rect.bottom - self.height_black_line, self.rect.width, self.height_black_line))

    def draw_number(self, surface):
        number_rect_width = 20
        number_rect_height = 16
        if self.time > 0:
            self.number_color = (0, 255, 0)
            number_rect_position = pygame.Rect(self.rect.right - number_rect_width - 10,
                                    self.rect.centery - (number_rect_height / 2),
                                    number_rect_width, number_rect_height)
        else:
            self.number_color = (0, 0, 0)
            number_rect_position = pygame.Rect(self.rect.centerx - (number_rect_width / 2),
                                    self.rect.centery - (number_rect_height / 2),
                                    number_rect_width, number_rect_height)
        pygame.draw.rect(surface, (192, 192, 192), number_rect_position)

        number_text = self.font.render(str(self.number), True, self.number_color)
        text_rect = number_text.get_rect(center=number_rect_position.center)
        surface.blit(number_text, text_rect)

    def draw_timer(self, surface):
        timer_text = self.font.render(f"{self.time:.1f}", True, (255, 255, 255))
        timer_rect = timer_text.get_rect(midtop=(self.rect.left + 20, self.rect.top + 10))
        surface.blit(timer_text, timer_rect)

    def process_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and self.press == False:
            return self.number
        return -1

    def get_rect(self):
        return self.rect

    def timer(self, current_time, last_time):
        if self.time > 0:
            self.time -= current_time-last_time
        else:
            self.time = 0

    def increment_timer(self, time_to_add):
        if self.time < 0:
            self.time = time_to_add
        else:
            self.time += time_to_add