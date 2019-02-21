import pygame
import model

# A class that manages all the events occuring throughout the game
class EventManager:

    def __init__(self, window_manager):
        self.state = "Menu"
        self.window_manager = window_manager
        self.model = None


    def manageEvent(self, event):
        if self.state == "Menu":
            self.manageMenu(event)
        if self.state == "Roulette":
            self.manageRoulette(event)


    def startGame(self, prng):
        self.model = model.Model(prng)
        self.state = "Roulette"
        self.window_manager.initRoulette()
        self.window_manager.initSideMenu(self.model)


    def manageMenu(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_F1):
            self.startGame("lfsr")
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_F2):
            self.startGame("mt")
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_F3):
            self.startGame("mt_truncated")


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
        
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_t):
            self.fast_forward()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # handle click on launch button
            if self.window_manager.launch_button.rect.collidepoint(event.pos):
                event_kspace = pygame.event.Event(pygame.KEYDOWN)
                event_kspace.key = pygame.K_SPACE
                self.manageRoulette(event_kspace)

            # handle click on fast forward button
            if self.window_manager.ff_button.rect.collidepoint(event.pos):
                self.fast_forward()

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

        elif event.type == pygame.MOUSEMOTION:
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

    def fast_forward(self): # Fast Forward
        mode = self.model.prng.mode
        if mode == "mt" or mode == "mt_truncated":
            self.state = "FF"

            nbOutputTarget = 624 * 8
            if mode == "mt_truncated":
                nbOutputTarget = 1248 * (8 - self.model.prng.nbDropped)

            f = open("demo_" + str(mode) + ".txt", "a+")

            while (self.model.prng.nbOutput < nbOutputTarget):
                self.model.compute_next_value() # compute next random pocket
                
                # do the increment animation on the counter AND on the wheel
                if self.model.prng.nbOutput % 14 == 0:
                    self.window_manager.window.blit(self.window_manager.fond_casino, (0, 0))
                    self.window_manager.blitSideMenu(self.model)
                    self.window_manager.wheel.change_angle(self.window_manager.wheel.angle + 10)
                    self.window_manager.blitWheel()
                    self.window_manager.blitArrow()
                    pygame.display.flip()
                    pygame.time.wait(1)

                # last iteration : set the correct angle to the wheel
                if self.model.prng.nbOutput == nbOutputTarget:
                    self.window_manager.window.blit(self.window_manager.fond_casino, (0, 0))
                    self.window_manager.blitSideMenu(self.model)
                    self.window_manager.wheel.change_angle(((self.model.nextValue - 4)%16)* 360/16)
                    self.window_manager.blitWheel()
                    self.window_manager.blitArrow()
                    pygame.display.flip()

                # write the value into a file
                f.write("{}\n".format(self.model.nextValue))

            f.close()

            self.window_manager.blitSideMenu(self.model)
            pygame.event.clear() # clear all events that happened while the wheel was rolling
            self.state = "Roulette"

            pygame.display.flip()
