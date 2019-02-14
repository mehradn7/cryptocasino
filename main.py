#!/usr/bin/python3
import random
import pygame

import events
import view.interface as  interface
import rng.randomNumber as randomNumber
import utils

def mainLoop(mode="lfsr"):
    print("Init pygame mainloop")
    pygame.init()

    running = True
    clock = pygame.time.Clock()
    window_manager = interface.WindowManager()
    window_manager.initMainMenu()
    event_manager = events.EventManager(window_manager, mode)

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                event_manager.manageEvent(event)
        
    print("Fin")

def testRNG(mode="lfsr"):
    print("Test of RNG : "+mode)
    prng = randomNumber.PRNG(mode, random.SystemRandom().getrandbits(32))
    for i in range(10):
        a = prng.randomNumber_4bits()
        print(utils.intToBits(a, 4))


if __name__ == "__main__":
    # execute only if run as a script
    mainLoop("lfsr")
    #testRNG("lfsr")
    #testRNG("mersenne twister")