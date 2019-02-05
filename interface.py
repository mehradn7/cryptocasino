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
        self.fond_casino = pygame.image.load(image_fond_casino).convert()
        self.fond_roulette = pygame.image.load(image_fond_roulette).convert()
        self.fond_sidemenu = pygame.image.load(image_fond_sidemenu).convert()
        self.wheel = Wheel()
        self.wheelAngle = 0
        self.arrow = pygame.image.load(image_arrow).convert_alpha()


    def initMenu(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_casino, (0,0))
        pygame.display.flip()

    def initRoulette(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_casino, (0,0))
        self.window.blit(self.fond_sidemenu, (768,0))
        self.wheel.change_angle(360 / 32)
        self.window.blit(self.wheel.surface, (34 + 349 - self.wheel.center_x, 34 + 349 - self.wheel.center_y))
        self.window.blit(self.arrow, (710,359))
        pygame.display.flip()

    def roll(self):

        nbRot =  150
        init_angle = self.wheel.angle
        end_angle = (self.wheel.angle + 360/16)%360 # à changer en random (PRNG)

        time = numpy.linspace(0,numpy.pi/2, nbRot)
        
        angles_test = [numpy.sin(x) for x in time]
        
        angles_test = [((end_angle + 4 *360 - init_angle))*x for x in angles_test]

        angles_test = [init_angle + x for x in angles_test]
        
        print(angles_test)

        for i in range(1, nbRot):
            self.window.blit(self.fond_casino, (0,0))
            self.window.blit(self.fond_sidemenu, (768,0))
            self.wheel.change_angle(angles_test[i])
            self.window.blit(self.wheel.surface, (34 + 349 - self.wheel.center_x, 34 + 349 - self.wheel.center_y)) # afficher la roue
            self.window.blit(self.arrow, (710,359)) # afficher la flèche
            pygame.display.flip()
            #pygame.time.wait(5 + (5* i**2)//nbRot)
            pygame.time.wait(5)

