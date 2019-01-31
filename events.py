import pygame
import interface

class EventManager:

    def __init__(self, windowManager):
        self.state = "Menu"
        self.windowManager = windowManager

    def manageEvent(self, event):
        if (self.state == "Menu"):
            self.manageMenu(event)
        if (self.state == "Roulette"):
            self.manageRoulette(event)

    def manageMenu(self,event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):  
            self.state = "Roulette"
            self.windowManager.initRoulette()

    def manageRoulette(self,event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  
            self.state = "Menu"
            self.windowManager.initMenu()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            self.state = "Rolling"
            self.windowManager.roll()
            pygame.time.wait(100)
            self.state = "Roulette"
