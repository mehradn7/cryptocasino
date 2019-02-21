#!/usr/bin/python3
import random
import pygame

import events
import view.interface as  interface
import rng.randomNumber as randomNumber
import utils

def mainLoop():
    print("Init pygame mainloop")
    pygame.init()

    running = True
    clock = pygame.time.Clock()
    window_manager = interface.WindowManager()
    window_manager.initMainMenu()
    event_manager = events.EventManager(window_manager)

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                event_manager.manageEvent(event)
        
    print("Fin")

def testRNG(mode="lfsr"):
    print("Test of RNG : " + mode)
    prng = randomNumber.PRNG(mode, random.SystemRandom().getrandbits(32))
    for i in range(10):
        a = prng.randomNumber_4bits()
        print(utils.intToBits(a, 4))

def testWriteOutput(mode="mt", nbOut = 8*624, filename = "demo1.txt"):
    print("Writing values of RNG : "+mode)
    prng = randomNumber.PRNG(mode, random.SystemRandom().getrandbits(32))

    with open(filename, 'w') as filemt:
        for i in range(nbOut):
            filemt.write("{}\n".format(prng.randomNumber_4bits()))


if __name__ == "__main__":
    # execute only if run as a script
    mainLoop()
    #testRNG("lfsr")
    #testRNG("mersenne twister")
    #testWriteOutput(nbOut=8*625)