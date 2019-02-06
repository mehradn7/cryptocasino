#!/usr/bin/python3
import pygame
import events
import interface
import randomNumber
import random
import utils

def mainLoop(mode = "lfsr"):
    print("Init pygame mainloop")
    pygame.init()
    
    running = True
    clock = pygame.time.Clock()
    windowManager = interface.windowManager()
    windowManager.initMainMenu()
    eventManager = events.EventManager(windowManager, mode)

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                eventManager.manageEvent(event)
        
    print("Fin")

def testRNG(mode ="lfsr"):
    print("Test of RNG : "+mode)
    prng = randomNumber.PRNG(mode, random.SystemRandom().getrandbits(32))
    for i in range(10):
        a = prng.randomNumber_4bits()
        print(utils.intToBits(a, 4))


if __name__ == "__main__":
    # execute only if run as a script
    mode  ="lfsr"
    mainLoop(mode)
    #testRNG("lfsr")
    #testRNG("mersenne twister")