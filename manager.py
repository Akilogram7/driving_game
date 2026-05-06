import pygame
pygame.init()

#Game Setup 
fps = 60
fpsClock = pygame.time.Clock()
info = pygame.display.Info()
WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h

screen = "start"
font = pygame.font.SysFont('Comic sans', 28)
