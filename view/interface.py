import pygame
import numpy

from params import *
import view.pocketbutton as pocketbutton
import view.betbutton as betbutton
import view.wheel as wheel

# A class representing the window and all its content
class WindowManager:
    def __init__(self):
        self.window = pygame.display.set_mode((width, height))
        self.fond_casino = pygame.image.load(image_fond_casino).convert()
        self.fond_roulette = pygame.image.load(image_fond_roulette).convert()
        self.fond_sidemenu = pygame.image.load(image_fond_sidemenu).convert()
        self.wheel = wheel.Wheel()
        self.wheelAngle = 0
        self.arrow = pygame.transform.scale(pygame.image.load(image_arrow).convert_alpha(), (arrowSide*3 //2 ,arrowSide))
        self.pocket_sprites = pygame.sprite.Group()
        self.bet_sprites = pygame.sprite.Group()
        self.list_images_buttons_normal = []
        self.list_images_buttons_clicked = []
        self.list_images_mises_normal = []
        self.list_images_mises_clicked = []

        for i in range(16):
            self.list_images_buttons_normal.append(pygame.transform.scale(pygame.image.load(images_buttons_normal[i]).convert_alpha(), (300,200)))
            self.list_images_buttons_clicked.append(pygame.transform.scale(pygame.image.load(images_buttons_clicked[i]).convert_alpha(), (300,200)))
        for i in range(4):
            self.list_images_mises_normal.append(pygame.transform.scale(pygame.image.load(images_mises_normal[i]).convert_alpha(), (300,300)))
            self.list_images_mises_clicked.append(pygame.transform.scale(pygame.image.load(images_mises_clicked[i]).convert_alpha(), (300,300)))

    def initMainMenu(self):
        pygame.display.set_caption(title)
        self.window.blit(self.fond_casino, (0,0))
        pygame.display.flip()

    def createPocketButton(self, modele, i, j):
        pocketNumber = 4*i+j
        button = pocketbutton.PocketButton(height + 10 + 60*j, 150 + 40*i, 55, 35,self.list_images_buttons_normal[pocketNumber], 
        self.list_images_buttons_clicked[pocketNumber], self.list_images_buttons_clicked[pocketNumber], pocketNumber)
        self.pocket_sprites.add(button)
        button.update_picture(modele)

    def createBetButton(self, modele, value, i):
        button = betbutton.BetButton(height + 10 + 60*i, 380, 55, 55,self.list_images_mises_normal[i], 
        self.list_images_mises_clicked[i], self.list_images_mises_clicked[i], value)
        self.bet_sprites.add(button)
        button.update_picture(modele)

    def initSideMenu(self, modele):

        # create button sprites
        # pocketButtons
        for i in range(4):
            for j in range(4):
                self.createPocketButton(modele, i, j)
        # betButtons
        betValues = [10, 20, 50, 100]
        for i in range(4):
            self.createBetButton(modele, betValues[i], i)            


        self.blitSideMenu(modele)

        pygame.display.flip()

    def blitSideMenu(self, modele):
        self.window.blit(self.fond_sidemenu, (height,0))

        # draw section titles
        font = pygame.font.SysFont("Stilton", 42)
        textyellow = (242, 255, 0)

        gainsLabel = font.render("Balance : ${}".format(modele.balance), 1, textyellow)
        self.window.blit(gainsLabel, (height + 20, 40))

        caseLabel = font.render("Pocket", 1, textyellow)
        self.window.blit(caseLabel, (height + 80, 100))

        miseLabel = font.render("Bet", 1, textyellow)
        self.window.blit(miseLabel, (height + 100, 340 ))
        launchButton = pygame.image.load(image_launchbutton).convert_alpha()
        self.window.blit(launchButton, (height + 5, 500))

        # draw button sprites
        self.pocket_sprites.draw(self.window)
        self.bet_sprites.draw(self.window)



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

    def roll(self, nextValue, modele):
        nbRot =  150
        init_angle = self.wheel.angle
        end_angle = ((nextValue - 4)%16)* 360/16

        time = numpy.linspace(0,numpy.pi/2, nbRot)
        angle_values = [numpy.sin(x) for x in time]
        angle_values = [((end_angle + 4 *360 - init_angle))*x for x in angle_values]
        angle_values = [init_angle + x for x in angle_values]
        for i in range(1, nbRot):
            self.window.blit(self.fond_casino, (0,0))
            self.blitSideMenu(modele)
            self.wheel.change_angle(angle_values[i])
            self.blitWheel()
            self.blitArrow()
            pygame.display.flip()
            #pygame.time.wait(5 + (5* i**2)//nbRot)
            pygame.time.wait(5)