#!/usr/bin/python3
import pygame
import events
import interface


def mainLoop():
    print("Test")
    pygame.init()
    
    running = True
    clock = pygame.time.Clock()
    windowManager = interface.windowManager()
    windowManager.initMenu()
    eventManager = events.EventManager(windowManager)

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        else:
            eventManager.manageEvent(event)
        
    print("Fin")


if __name__ == "__main__":
    # execute only if run as a script
    mainLoop()