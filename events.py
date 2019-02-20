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
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            self.state = "Rolling"

            self.model.compute_next_value() # compute next random pocket
            self.window_manager.roll(self.model) # roll the roulette
            
            # write the value into a file
            if self.model.prng.mode == "mt" or self.model.prng.mode == "mt_truncated":
                f = open("demo_" + str(self.model.prng.mode) + ".txt", "a+")
                f.write("{}\n".format(self.model.nextValue))
                f.close()
            self.model.play_turn() # update the game model
            self.model.set_bet(model.Model.bet_values[0]) # set the selected bet to the minimal bet
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

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_t):
            # Fast Forward     
            mode = self.model.prng.mode        
            if mode == "mt" or mode == "mt_truncated":
                self.state = "FF"

                nbOutputTarget = 624 * 8
                if mode == "mt_truncated":
                    nbOutputTarget = 1248 * (8 - self.model.prng.nbDropped)

                f = open("demo_" + str(mode) + ".txt", "a+")

                #self.window_manager.simulate_fast_forward(self.model, nbOutputTarget)

                while (self.model.prng.nbOutput < nbOutputTarget):
                    self.model.compute_next_value() # compute next random pocket
                    self.window_manager.blitSideMenu(self.model)

                    # do the increment animation
                    if self.model.prng.nbOutput % 11 == 0:
                        pygame.display.flip()
                        pygame.time.wait(1)

                    # write the value into a file
                    f.write("{}\n".format(self.model.nextValue))
                
                f.close()

                self.window_manager.blitSideMenu(self.model)
                pygame.event.clear() # clear all events that happened while the wheel was rolling
                self.state = "Roulette"

                pygame.display.flip()