import pygame
import numpy
from params import *
from button import *

# A class representing the wheel
class Wheel: # mettre dans un fichier à part
    def __init__(self):
        self.surface = pygame.image.load(image_wheel).convert_alpha()
        self.angle = 0
        self.center_x = wheelRadius
        self.center_y = wheelRadius

    def change_angle(self, angle):
        self.angle = angle % 360
        self.surface = pygame.transform.rotate(pygame.image.load(image_wheel).convert_alpha(), self.angle)
        self.center_x, self.center_y = self.surface.get_rect().center

# A class representing the game and all its content
class windowManager: #changer le nom en 'Game' (et renommer ce fichier en game.py), ça parait plus logique : non
    def __init__(self):
        self.window = pygame.display.set_mode((width, height))
        self.fond_casino = pygame.image.load(image_fond_casino).convert()
        self.fond_roulette = pygame.image.load(image_fond_roulette).convert()
        self.fond_sidemenu = pygame.image.load(image_fond_sidemenu).convert()
        self.wheel = Wheel()
        self.wheelAngle = 0
        self.arrow = pygame.transform.scale(pygame.image.load(image_arrow).convert_alpha(), (arrowSide*3 //2 ,arrowSide))
        self.case_sprites = pygame.sprite.Group()
        self.list_images_buttons_normal = []
        self.list_images_buttons_clicked = []

        for i in range(16):
            self.list_images_buttons_normal.append(pygame.transform.scale(pygame.image.load(images_buttons_normal[i]).convert_alpha(), (300,200)))
            self.list_images_buttons_clicked.append(pygame.transform.scale(pygame.image.load(images_buttons_clicked[i]).convert_alpha(), (300,200)))

    def initMainMenu(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_casino, (0,0))
        pygame.display.flip()

    def initSideMenu(self, modele):

        # create button sprites
        for i in range(4):
            for j in range(4):
                caseNumber = 4*i+j
                button = CaseButton(height + 10 + 60*j, 160 + 40*i, 55, 35,self.list_images_buttons_normal[caseNumber], 
                self.list_images_buttons_clicked[caseNumber], self.list_images_buttons_clicked[caseNumber], caseNumber)
                self.case_sprites.add(button)
                button.update_picture(modele)
                
        self.blitSideMenu()

        pygame.display.flip()

    def blitSideMenu(self, gain = 100):
        self.window.blit(self.fond_sidemenu, (height,0))

        # draw section titles
        font = pygame.font.SysFont("Ubuntu", 36)

        gainsLabel = font.render("Gains", 1, (0,0,0))
        self.window.blit(gainsLabel, (height + 80,10))

        caseLabel = font.render("Case", 1, (0,0,0))
        self.window.blit(caseLabel, (height + 80,100))

        miseLabel = font.render("Mise", 1, (0,0,0))
        self.window.blit(miseLabel, (height + 80,5*height/8 ))
        launchButton = pygame.image.load(image_launchbutton).convert_alpha()
        self.window.blit(launchButton, (height + 5,7*height/8))

        # draw button sprites
        self.case_sprites.draw(self.window)


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
        self.window.blit(self.arrow, (wheelShift + wheelDiameter - arrowSide,(height-arrowSide)/2))

    def roll(self, nextValue):
        nbRot =  150
        init_angle = self.wheel.angle
        end_angle = ((nextValue - 4)%16)* 360/16

        time = numpy.linspace(0,numpy.pi/2, nbRot)
        angle_values = [numpy.sin(x) for x in time]
        angle_values = [((end_angle + 4 *360 - init_angle))*x for x in angle_values]
        angle_values = [init_angle + x for x in angle_values]
        for i in range(1, nbRot):
            self.window.blit(self.fond_casino, (0,0))
            self.blitSideMenu()
            self.wheel.change_angle(angle_values[i])
            self.blitWheel()
            self.blitArrow()
            pygame.display.flip()
            #pygame.time.wait(5 + (5* i**2)//nbRot)
            pygame.time.wait(5)