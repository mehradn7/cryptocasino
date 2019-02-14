import pygame

import model

# A class that manages all the events occuring throughout the game
class EventManager:

    def __init__(self, windowManager, prngMode = "lfsr"):
        self.state = "Menu"
        self.windowManager = windowManager
        self.modele = model.Model(prngMode)


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
            # BUG : REDESSINER LA ROUE CORRECTEMENT

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            self.state = "Rolling"

            self.modele.compute_next_value()
            print("Next", self.modele.nextValue)
            self.windowManager.roll(self.modele)
            self.modele.play_turn()
            self.modele.mise = 10
            self.windowManager.blitSideMenu(self.modele)

            # check if game is over
            if (self.modele.balance <= 0):
                print("GAME OVER")
                #to do restart game
            else:
                pygame.event.clear() # clear all events that happened while the wheel was rolling
                self.state = "Roulette"

            pygame.display.flip()

        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (self.windowManager.launch_button.rect.collidepoint(event.pos)):
                event_kspace = pygame.event.Event(pygame.KEYDOWN)
                event_kspace.key = pygame.K_SPACE
                self.manageRoulette(event_kspace)

            # handle click to update the model (pocket_sprites)
            for pocket_button in self.windowManager.pocket_sprites.sprites():
                if pocket_button.rect.collidepoint(event.pos):
                    self.modele.caseChosen(pocket_button.pocketNumber)

            # handle click to update the model (bet_sprites)
            for bet_button in self.windowManager.bet_sprites:
                if bet_button.rect.collidepoint(event.pos):
                    self.modele.miseChosen(bet_button.betValue)
            

            # update pictures depending on the model
            for pocket_button in self.windowManager.pocket_sprites.sprites():
                pocket_button.update_picture(self.modele)
            for bet_button in self.windowManager.bet_sprites:
                bet_button.update_picture(self.modele)

            # refresh view
            self.windowManager.pocket_sprites.draw(self.windowManager.window)
            for sprite in self.windowManager.bet_sprites:
                if sprite.betValue <= self.modele.balance: # draw the bet sprite only if the player has sufficient money
                    self.windowManager.window.blit(sprite.image, sprite.rect)

            pygame.display.flip()

        if (event.type == pygame.MOUSEMOTION):
            # handle click to update the model (pocket_sprites)
            for button in self.windowManager.pocket_sprites.sprites():
                
                if self.modele.case != button.pocketNumber:
                    if button.rect.collidepoint(event.pos):
                        button.image = button.image_hover
                    else:
                        button.image = button.image_normal

            # refresh view
            self.windowManager.pocket_sprites.draw(self.windowManager.window)
            pygame.display.flip()
