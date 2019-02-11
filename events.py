import pygame
import crypto.randomNumber
import model

# A class that manages all the events occuring throughout the game
class EventManager:

    def __init__(self, windowManager, prngMode = "lfsr"):
        self.state = "Menu"
        self.windowManager = windowManager
        self.prng = crypto.randomNumber.PRNG(prngMode)
        self.modele = model.Model()


    def manageEvent(self, event):
        if (self.state == "Menu"):
            self.manageMenu(event)
        if (self.state == "Roulette"):
            self.manageRoulette(event)

    def manageMenu(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):  
            self.state = "Roulette"
            self.windowManager.initRoulette()
            self.windowManager.initSideMenu(self.modele)

    def manageRoulette(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  
            self.state = "Menu"
            self.windowManager.initMainMenu()
            
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            self.state = "Rolling"
            nextValue = self.prng.randomNumber_4bits()
            print("Next", nextValue)
            self.windowManager.roll(nextValue)
            self.modele.tour(nextValue)
            pygame.event.clear() # clear all events that happened while the wheel was rolling
            self.state = "Roulette"

        if (event.type == pygame.MOUSEBUTTONDOWN):

            # handle click to update the model (case_sprites)
            for button in self.windowManager.case_sprites.sprites():
                if button.rect.collidepoint(event.pos):
                    self.modele.caseChosen(button.pocketNumber)

            # handle click to update the model (bet_sprites)
    
            # update pictures depending on the model
            for button in self.windowManager.case_sprites.sprites():
                button.update_picture(self.modele)
    
            # refresh view
            self.windowManager.case_sprites.draw(self.windowManager.window)
            pygame.display.flip()

        if (event.type == pygame.MOUSEMOTION):
            # handle click to update the model (case_sprites)
            for button in self.windowManager.case_sprites.sprites():
                
                if self.modele.case != button.pocketNumber:
                    if button.rect.collidepoint(event.pos):
                        button.image = button.image_hover
                    else:
                        button.image = button.image_normal

            # refresh view
            self.windowManager.case_sprites.draw(self.windowManager.window)
            pygame.display.flip()
