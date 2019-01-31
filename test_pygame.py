import pygame
from pygame.locals import *

pygame.init()

#Chargement et collage du fond
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("../Images/tls-sec.png").convert()
fenetre.blit(fond, (0,0))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	continuer = int(input())
