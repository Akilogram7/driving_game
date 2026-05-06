import pygame, sys, manager

def output(window):
    
    
    def display():
        window.fill((255,255,255))
        
    run = True 
    while run: 
        display()
        for event in pygame.event.get():
            # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw       
        