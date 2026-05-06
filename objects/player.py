import pygame
import objects.images, manager
import math

class movable(objects.images.still):
    def __init__(self, x, y,width,height,image_to_use, speed):
        super().__init__(x, y,width,height,image_to_use)
        self.speed = speed 
        
    def key_press(self):
        key_input = pygame.key.get_pressed()
        #checks if the player is pressing the a or d key
        if key_input[pygame.K_LSHIFT]:  
            self.speed = 9
            
        elif not key_input[pygame.K_LSHIFT]: 
            self.speed = 4

        self.movex = (key_input[pygame.K_a] * -self.speed) + (key_input[pygame.K_d] * self.speed)
        self.movey = (key_input[pygame.K_w] * -self.speed) + (key_input[pygame.K_s] * self.speed)
        self.rect.move_ip(self.movex, self.movey)


    def back(self):
        if self.rect.x <= 0 or self.rect.y <= 0:
            self.rect.x -= self.movex+10*-1
            self.rect.y -= self.movey+10*-1
        elif self.rect.x >= manager.WINDOW_WIDTH or self.rect.y >= manager.WINDOW_HEIGHT:
            self.rect.x -= self.movex+10*1
            self.rect.y -= self.movey+10*1
    
    # def wall_collision(self):
    #     self.rect.x -= self.movex
    #     self.rect.y -= self.movey