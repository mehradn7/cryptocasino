import pygame
import numpy
from params import *

class Wheel:
    def __init__(self):
        self.surface = pygame.image.load(image_wheel).convert_alpha()
        self.angle = 0
        self.center_x = 349
        self.center_y = 349

    def change_angle(self, angle):
        self.angle = angle % 360
        self.surface = pygame.transform.rotate(pygame.image.load(image_wheel).convert_alpha(), self.angle)
        self.center_x, self.center_y = self.surface.get_rect().center

class windowManager:

    def __init__(self):
        self.window = pygame.display.set_mode((width, height))
        self.fond_roulette = pygame.image.load(image_fond_roulette).convert()
        self.fond_sidemenu = pygame.image.load(image_fond_sidemenu).convert()
        self.wheel = Wheel()
        self.wheelAngle = 0
        self.arrow = pygame.image.load(image_arrow).convert_alpha()


    def initMenu(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_roulette, (0,0))
        self.window.blit(self.fond_sidemenu, (768,0))
        pygame.display.flip()

    def initRoulette(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_roulette, (0,0))
        self.window.blit(self.fond_sidemenu, (768,0))
        self.wheel.change_angle(360 / 32)
        self.window.blit(self.wheel.surface, (34 + 349 - self.wheel.center_x, 34 + 349 - self.wheel.center_y))
        self.window.blit(self.arrow, (710,359))
        pygame.display.flip()

    def roll(self):

        nbRot = 40
        init_angle = self.wheel.angle
        end_angle = (self.wheel.angle + 360/16)%360
        positions = numpy.linspace(init_angle, end_angle + 4 *360, nbRot)
        for i in range(1, nbRot):
            self.window.blit(self.fond_roulette, (0,0))
            self.wheel.change_angle(positions[i])
            self.window.blit(self.wheel.surface, (34 + 349 - self.wheel.center_x, 34 + 349 - self.wheel.center_y))
            self.window.blit(self.arrow, (710,359))
            pygame.display.flip()
            pygame.time.wait(5 + (5* i**2)//nbRot)

