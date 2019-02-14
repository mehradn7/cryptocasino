import pygame

from params import WHEEL_RADIUS, IMAGE_WHEEL

# A class representing the wheel
class Wheel:
    def __init__(self):
        self.surface = pygame.image.load(IMAGE_WHEEL).convert_alpha()
        self.angle = 0
        self.center_x = WHEEL_RADIUS
        self.center_y = WHEEL_RADIUS

    def change_angle(self, angle):
        self.angle = angle % 360
        self.surface = pygame.transform.rotate(pygame.image.load(IMAGE_WHEEL).convert_alpha(), self.angle)
        self.center_x, self.center_y = self.surface.get_rect().center
