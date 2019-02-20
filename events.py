import pygame

import model

# A class that manages all the events occuring throughout the game
class EventManager:

    def __init__(self, window_manager, prngMode="lfsr"):
        self.state = "Menu"
        self.window_manager = window_manager
        self.model = model.Model(prngMode)


    def manageEvent(self, event):
        if self.state == "Menu":
            self.manageMenu(event)
        if self.state == "Roulette":
            self.manageRoulette(event)

    def manageMenu(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):
            self.state = "Roulette"
            self.window_manager.initRoulette()
            self.window_manager.initSideMenu(self.model)

    def manageRoulette(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.state = "Menu"
            self.window_manager.initMainMenu()
            # BUG : REDESSINER LA ROUE CORRECTEMENT

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            self.state = "Rolling"

            self.model.compute_next_value()
            print("Next", self.model.nextValue)
            self.window_manager.roll(self.model)
            self.model.play_turn()
            self.model.bet = model.Model.bet_values[0]
            self.window_manager.blitSideMenu(self.model)

            # check if game is over
            if (self.model.balance <= 0):
                print("GAME OVER")
                self.window_manager.blitGameOver()
                #to do restart game
            else:
                pygame.event.clear() # clear all events that happened while the wheel was rolling
                self.state = "Roulette"

            pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.window_manager.launch_button.rect.collidepoint(event.pos):
                event_kspace = pygame.event.Event(pygame.KEYDOWN)
                event_kspace.key = pygame.K_SPACE
                self.manageRoulette(event_kspace)

            # handle click to update the model (pocket_sprites)
            for pocket_button in self.window_manager.pocket_sprites.sprites():
                if pocket_button.rect.collidepoint(event.pos):
                    self.model.set_pocket(pocket_button.pocketNumber)

            # handle click to update the model (bet_sprites)
            for bet_button in self.window_manager.bet_sprites:
                if bet_button.rect.collidepoint(event.pos):
                    self.model.set_bet(bet_button.betValue)

            # update pictures depending on the model
            for pocket_button in self.window_manager.pocket_sprites.sprites():
                pocket_button.update_picture(self.model)
            for bet_button in self.window_manager.bet_sprites:
                bet_button.update_picture(self.model)

            # refresh view
            self.window_manager.pocket_sprites.draw(self.window_manager.window)
            for sprite in self.window_manager.bet_sprites:
                if sprite.betValue <= self.model.balance: # draw the bet sprite only if the player has sufficient money
                    self.window_manager.window.blit(sprite.image, sprite.rect)

            pygame.display.flip()

        if event.type == pygame.MOUSEMOTION:
            # handle click to update the model (pocket_sprites)
            for button in self.window_manager.pocket_sprites.sprites():  
                if self.model.pocket != button.pocketNumber:
                    if button.rect.collidepoint(event.pos):
                        button.image = button.image_hover
                    else:
                        button.image = button.image_normal

            # refresh view
            self.window_manager.pocket_sprites.draw(self.window_manager.window)
            pygame.display.flip()
