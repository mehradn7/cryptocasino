import pygame
import numpy

from params import *
import view.pocketbutton as pocketbutton
import view.betbutton as betbutton
import view.button as button
import view.wheel as wheel

# A class representing the window and all its content
class WindowManager:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.fond_casino = pygame.image.load(IMAGE_FOND_CASINO).convert()
        self.fond_roulette = pygame.image.load(IMAGE_FOND_ROULETTE).convert()
        self.fond_sidemenu = pygame.image.load(IMAGE_FOND_SIDEMENU).convert()
        self.wheel = wheel.Wheel()
        self.arrow = pygame.transform.scale(pygame.image.load(IMAGE_ARROW).convert_alpha(), (ARROW_SIDE*3 //2, ARROW_SIDE))
        self.pocket_sprites = pygame.sprite.Group()
        self.bet_sprites = []
        self.list_images_buttons_normal = []
        self.list_images_buttons_clicked = []
        self.list_images_mises_normal = []
        self.list_images_mises_clicked = []
        self.launch_button = button.Button(WINDOW_HEIGHT + 5, 500, 246, 80, pygame.image.load(IMAGE_LAUNCHBUTTON).convert_alpha(),
        pygame.image.load(IMAGE_LAUNCHBUTTON).convert_alpha(), pygame.image.load(IMAGE_LAUNCHBUTTON).convert_alpha())

        for i in range(16):
            self.list_images_buttons_normal.append(pygame.transform.scale(pygame.image.load(IMAGES_BUTTONS_NORMAL[i]).convert_alpha(), (300, 200)))
            self.list_images_buttons_clicked.append(pygame.transform.scale(pygame.image.load(IMAGES_BUTTONS_CLICKED[i]).convert_alpha(), (300, 200)))
        for i in range(4):
            self.list_images_mises_normal.append(pygame.transform.scale(pygame.image.load(IMAGES_MISES_NORMAL[i]).convert_alpha(), (300, 300)))
            self.list_images_mises_clicked.append(pygame.transform.scale(pygame.image.load(IMAGES_MISES_CLICKED[i]).convert_alpha(), (300, 300)))

    def initMainMenu(self):
        pygame.display.set_caption(GAME_TITLE)
        self.window.blit(self.fond_casino, (0, 0))
        pygame.display.flip()

    def createPocketButton(self, model, i, j):
        pocket_number = 4*i+j # row i, column j
        
        pocket_button = pocketbutton.PocketButton(WINDOW_HEIGHT + 10 + 60*j, 150 + 40*i, POCKET_BUTTON_WIDTH, POCKET_BUTTON_HEIGHT,
        self.list_images_buttons_normal[pocket_number], self.list_images_buttons_clicked[pocket_number],
        self.list_images_buttons_clicked[pocket_number], pocket_number)

        self.pocket_sprites.add(pocket_button)
        pocket_button.update_picture(model)

    def createBetButton(self, model, value, i):
        bet_button = betbutton.BetButton(WINDOW_HEIGHT + 10 + 60*i, 380, BET_BUTTON_WIDTH, BET_BUTTON_HEIGHT, self.list_images_mises_normal[i],
        self.list_images_mises_clicked[i], self.list_images_mises_clicked[i], value)
        
        self.bet_sprites.append(bet_button)
        bet_button.update_picture(model)

    def initSideMenu(self, model):

        # create button sprites
        # pocketButtons
        for i in range(4):
            for j in range(4):
                self.createPocketButton(model, i, j)
        # betButtons
        for i in range(4):
            self.createBetButton(model, model.bet_values[i], i)

        self.blitSideMenu(model)

        pygame.display.flip()

    def blitSideMenu(self, model):
        self.window.blit(self.fond_sidemenu, (WINDOW_HEIGHT, 0))

        # draw section titles
        font = pygame.font.SysFont("Uroob", 42)
        textyellow = (242, 255, 0)

        gainsLabel = font.render("Balance : ${}".format(model.balance), 1, textyellow)
        self.window.blit(gainsLabel, (WINDOW_HEIGHT + 20, 40))

        caseLabel = font.render("Pocket", 1, textyellow)
        self.window.blit(caseLabel, (WINDOW_HEIGHT + 80, 100))

        miseLabel = font.render("Bet", 1, textyellow)
        self.window.blit(miseLabel, (WINDOW_HEIGHT + 100, 340))

        # draw launch button
        self.window.blit(self.launch_button.image, self.launch_button.rect)

        # draw pocket sprites
        self.pocket_sprites.draw(self.window)

        # draw bet sprites
        for sprite in self.bet_sprites:
            if sprite.betValue <= model.balance: # draw the bet sprite only if the player has sufficient money
                sprite.update_picture(model)
                self.window.blit(sprite.image, sprite.rect)

    def initRoulette(self):
        pygame.display.set_caption(GAME_TITLE)
        self.window.blit(self.fond_casino, (0,0))
        self.wheel.change_angle(1)
        self.blitWheel()
        self.blitArrow()
        pygame.display.flip()

    def blitWheel(self):
        self.window.blit(self.wheel.surface, (WHEEL_SHIFT + WHEEL_RADIUS - self.wheel.center_x, WHEEL_SHIFT + WHEEL_RADIUS - self.wheel.center_y))

    def blitArrow(self):
        self.window.blit(self.arrow, (WHEEL_SHIFT + WHEEL_DIAMETER - ARROW_SIDE, (WINDOW_HEIGHT - ARROW_SIDE)/2))

    def roll(self, model):
        nbRot = 150
        init_angle = self.wheel.angle
        end_angle = ((model.nextValue - 4)%16)* 360/16

        time = numpy.linspace(0, numpy.pi/2, nbRot)
        angle_values = [numpy.sin(x) for x in time]
        angle_values = [((end_angle + 4 *360 - init_angle))*x for x in angle_values]
        angle_values = [init_angle + x for x in angle_values]
        
        for i in range(1, nbRot):
            self.window.blit(self.fond_casino, (0, 0))
            self.blitSideMenu(model)
            self.wheel.change_angle(angle_values[i])
            self.blitWheel()
            self.blitArrow()
            pygame.display.flip()
            pygame.time.wait(5)
