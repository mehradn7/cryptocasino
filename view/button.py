import pygame

# This is a base class representing any type of button
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
 
    def update_picture(self, modele):
        pass