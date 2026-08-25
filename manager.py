import pygame
pygame.init()

#Game Setup 
fps = 60
fpsClock = pygame.time.Clock()
info = pygame.display.Info()
WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h

PLAYER_FORWARD = "images/player_forward.png"
PLAYER_BACKWARD = "images/player_backward.png"

PLAYER_UPWARD = "images/player_upward.png"
PLAYER_BACKUPWARD = "images/player_backupward.png"

PLAYER_UP = "images/player_up.png"
PLAYER_DOWN = "images/player_down.png"

screen = "start"
font = pygame.font.SysFont('Comic sans', 28)
