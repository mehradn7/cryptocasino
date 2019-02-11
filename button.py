import pygame

# This class represents a single button with a number, used to bet on a pocket
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,
                 image_normal, image_hover,
                 image_down):

        super().__init__()

        self.image_normal = pygame.transform.scale(image_normal, (width, height))
        self.image_hover = pygame.transform.scale(image_hover, (width, height))
        self.image_down = pygame.transform.scale(image_down, (width, height))

        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect(topleft=(x, y))
 
        self.button_down = False

    def update_picture(self, modele):
        pass

class CaseButton(Button):
    def __init__(self, x, y, width, height, 
                 image_normal, image_hover,
                 image_down, caseNumber):

        super().__init__(x, y, width, height,
                 image_normal, image_hover,
                 image_down)
        
        self.caseNumber = caseNumber   

    def update_picture(self, modele):
        if modele.case == self.caseNumber:
            self.button_down = True
            self.image = self.image_down
        else:
            self.button_down = False
            self.image = self.image_normal