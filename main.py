import pygame, sys, manager
import interfaces.start
pygame.init()

window = pygame.display.set_mode((manager.WINDOW_WIDTH, manager.WINDOW_HEIGHT))
pygame.display.set_caption("Driving Game")

while True: 
    if manager.screen == "start":
        interfaces.start.output(window)
    elif manager.screen == "exit":
        pygame.quit()
        sys.exit()
        