import pygame
import numpy
from params import *

class Wheel:
    def __init__(self):
        self.surface = pygame.image.load(image_wheel).convert_alpha()
        self.angle = 0
        self.center_x = wheelRadius
        self.center_y = wheelRadius

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


    def initMainMenu(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_casino, (0,0))
        pygame.display.flip()

    def initSideMenu(self):
        self.window.blit(self.fond_sidemenu, (height,0))

        testFont = pygame.font.SysFont("Ubuntu", 48)
        randNumLabel = testFont.render("Gains", 1, (0,0,0))
        self.window.blit(randNumLabel, (height + 80,10))
        randNumLabel2 = testFont.render("Case", 1, (0,0,0))
        self.window.blit(randNumLabel2, (height + 80,height/3 + 10))
        randNumLabel3 = testFont.render("Mise", 1, (0,0,0))
        self.window.blit(randNumLabel3, (height + 80,2*height/3 + 10))
        launchButton = pygame.image.load(image_launchbutton).convert_alpha()
        self.window.blit(launchButton, (height + 5,height -90))
        pygame.display.flip()

    def blitSideMenu(self):
        self.window.blit(self.fond_sidemenu, (height,0))

        testFont = pygame.font.SysFont("Ubuntu", 48)
        randNumLabel = testFont.render("Gains", 1, (0,0,0))
        self.window.blit(randNumLabel, (height + 80,10))
        randNumLabel2 = testFont.render("Case", 1, (0,0,0))
        self.window.blit(randNumLabel2, (height + 80,height/3 + 10))
        randNumLabel3 = testFont.render("Mise", 1, (0,0,0))
        self.window.blit(randNumLabel3, (height + 80,2*height/3 + 10))
        launchButton = pygame.image.load(image_launchbutton).convert_alpha()
        self.window.blit(launchButton, (height + 5,height -90))


    def initRoulette(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_casino, (0,0))
        self.wheel.change_angle(1)
        self.blitWheel()
        self.blitArrow()
        pygame.display.flip()

    def blitWheel(self):
        self.window.blit(self.wheel.surface, (wheelShift + wheelRadius - self.wheel.center_x, wheelShift + wheelRadius - self.wheel.center_y))

    def blitArrow(self):
        self.window.blit(self.arrow, (wheelShift + wheelDiameter - (arrowSide/2),(height-arrowSide)/2))

    def roll(self, nextValue):

        nbRot =  150
        init_angle = self.wheel.angle
        end_angle = ((nextValue - 4)%16)* 360/16

        time = numpy.linspace(0,numpy.pi/2, nbRot)
        angles_test = [numpy.sin(x) for x in time]
        angles_test = [((end_angle + 4 *360 - init_angle))*x for x in angles_test]
        angles_test = [init_angle + x for x in angles_test]
        for i in range(1, nbRot):
            self.window.blit(self.fond_casino, (0,0))
            self.blitSideMenu()
            self.wheel.change_angle(angles_test[i])
            self.blitWheel()
            self.blitArrow()
            pygame.display.flip()
            #pygame.time.wait(5 + (5* i**2)//nbRot)
            pygame.time.wait(5)

