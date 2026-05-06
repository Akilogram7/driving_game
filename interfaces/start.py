import pygame, sys, manager
import objects.player, objects.images, objects.buttons

def output(window):
    player = objects.player.movable(100, 100, 200, 250, "images/car.png", 5)
    
    def display():
        window.fill((255,255,255))
        player.draw(window)
        
    run = True 
    while run: 
        display()
        key_input = pygame.key.get_pressed()
        
        player.key_press()
    
        for event in pygame.event.get():
            # if user  QUIT then the screen will close
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw       
        