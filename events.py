import pygame
import interface
import randomNumber

class EventManager:

    def __init__(self, windowManager, prngMode = "lfsr"):
        self.state = "Menu"
        self.windowManager = windowManager
        self.prng = randomNumber.PRNG(prngMode)

    def manageEvent(self, event):
        if (self.state == "Menu"):
            self.manageMenu(event)
        if (self.state == "Roulette"):
            self.manageRoulette(event)

    def manageMenu(self,event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):  
            self.state = "Roulette"
            self.windowManager.initRoulette()
            self.windowManager.initSideMenu()

    def manageRoulette(self,event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  
            self.state = "Menu"
            self.windowManager.initMainMenu()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            self.state = "Rolling"
            nextValue = self.prng.randomNumber_4bits()
            print("Next", nextValue)
            self.windowManager.roll(nextValue)
            pygame.time.wait(100)
            self.state = "Roulette"

        if (event.type == pygame.MOUSEBUTTONDOWN):
            for button  in self.windowManager.all_sprites.sprites():
                if (button.rect.collidepoint(event.pos)):
                    button.handle_event(event)
                    self.windowManager.all_sprites.draw(self.windowManager.window)
                    pygame.display.flip()
