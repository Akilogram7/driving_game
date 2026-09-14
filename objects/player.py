import pygame
import objects.images, manager
import math


class movable(objects.images.still):
    def __init__(self, x, y, width, height, image_to_use, speed):
        super().__init__(x, y, width, height, image_to_use)

        self.speed = speed
        
        self.vel_y = 0
        self.gravity = 0.6 
        self.jump_strength = -15
        self.on_ground = False

        # Load player direction images
        self.image_forward = pygame.image.load(manager.PLAYER_FORWARD).convert_alpha()

        self.image_backward = pygame.image.load(manager.PLAYER_BACKWARD).convert_alpha()

        self.image_upward = pygame.image.load(manager.PLAYER_UPWARD).convert_alpha()

        self.image_backupward = pygame.image.load(manager.PLAYER_BACKUPWARD).convert_alpha()
        
        self.image_up = pygame.image.load(manager.PLAYER_UP).convert_alpha()
        
        self.image_down = pygame.image.load(manager.PLAYER_DOWN).convert_alpha()

        # Scale player direction images
        self.image_forward = pygame.transform.scale(self.image_forward, (width, height))

        self.image_backward = pygame.transform.scale(self.image_backward, (width, height))

        self.image_upward = pygame.transform.scale(self.image_upward, (width, height))

        self.image_backupward = pygame.transform.scale(self.image_backupward, (width, height))
        
        self.image_up = pygame.transform.scale(self.image_up, (width, height))
        
        self.image_down = pygame.transform.scale(self.image_down, (width, height))

    def key_press(self):
        key_input = pygame.key.get_pressed()

        # Change speed when holding Left Shift
        if key_input[pygame.K_LSHIFT]:
            self.speed = 9
        else:
            self.speed = 4

        # Change player image depending on direction

        if key_input[pygame.K_w] and key_input[pygame.K_d]:
            self.image = self.image_upward
            
        elif key_input[pygame.K_w] and key_input[pygame.K_a]:
            self.image = self.image_backupward

        elif key_input[pygame.K_s] and key_input[pygame.K_d]:
            self.image = self.image_forward
            
        elif key_input[pygame.K_s] and key_input[pygame.K_a]:
            self.image = self.image_backward
            
        elif key_input[pygame.K_a]:
            self.image = self.image_backward
        
        elif key_input[pygame.K_d]:
            self.image = self.image_forward
            
        elif key_input[pygame.K_w]:
            self.image = self.image_up
    
        elif key_input[pygame.K_s]:
            self.image = self.image_down
                    
        # Update mask after changing image
        self.mask = pygame.mask.from_surface(self.image)

        # Player movement
        self.movex = (key_input[pygame.K_a] * -self.speed + key_input[pygame.K_d] * self.speed)
        self.movey = (key_input[pygame.K_w] * -self.speed) + (key_input[pygame.K_s] * self.speed)

        # Jump
        if key_input[pygame.K_w] and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False

        # Gravity
        self.vel_y += self.gravity
        self.movey = self.vel_y

        # Move player
        self.rect.move_ip(self.movex, self.movey)

        # Ground collision
        if self.rect.bottom >= manager.WINDOW_HEIGHT:
            self.rect.bottom = manager.WINDOW_HEIGHT
            self.vel_y = 0
            self.on_ground = True
        
    def back(self):
        if self.rect.x <= 0 or self.rect.y <= 0:
            self.rect.x -= self.movex + 10 * -1
            self.rect.y -= self.movey + 10 * -1

        elif self.rect.x >= manager.WINDOW_WIDTH or self.rect.y >= manager.WINDOW_HEIGHT:
            self.rect.x -= self.movex + 10 *1
            self.rect.y -= self.movey + 10  *1

    # def wall_collision(self):
    #     self.rect.x -= self.movex
    #     self.rect.y -= self.movey
