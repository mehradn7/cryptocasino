import pygame

# This class represents a single button with a number, used to bet on a pocket
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, callback,
                 image_normal, image_hover,
                 image_down):

        super().__init__()

        self.image_normal = pygame.transform.scale(image_normal, (width, height))
        self.image_hover = pygame.transform.scale(image_hover, (width, height))
        self.image_down = pygame.transform.scale(image_down, (width, height))

        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect(topleft=(x, y))
 
        # This function will be called when the button gets pressed.
        self.callback = callback
        self.button_down = False
    

    # Handle the click on a button
    def handle_event(self, event, modele):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.button_down = not (self.button_down)
                self.image = self.image_down if (self.button_down == True) else self.image_normal
            else:
                self.button_down = False
                self.image = self.image_normal
            self.callback()
        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal

    def update_picture(self, modele):
        pass

class CaseButton(Button):
    def __init__(self, x, y, width, height, callback,
                 image_normal, image_hover,
                 image_down, caseNumber):

        super().__init__(x, y, width, height, callback,
                 image_normal, image_hover,
                 image_down)
        
        self.caseNumber = caseNumber   

    # Handle the click on a button
    def handle_event(self, event, modele):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                modele.caseChosen(self.caseNumber)
            self.callback()

    def update_picture(self, modele):
        if modele.case == self.caseNumber:
            self.button_down = True
            self.image = self.image_down
        else:
            self.button_down = False
            self.image = self.image_normal