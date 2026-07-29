import pygame, sys, manager
import objects.player, objects.images, objects.buttons

def output(window):
    player = objects.player.movable(100, 100, 200, 250, "images/car.png", 5)
    btn_exit = objects.buttons.with_background(0, 0, 100, 100, 'Ariel', 50, (252, 28, 3), (0,0,0), (255, 133, 120), (255,255,255), "Exit")
    
    def display():
        window.fill((255,255,255))
        player.draw(window)
        btn_exit.draw(window)
        
    run = True 
    while run: 
        display()
        key_input = pygame.key.get_pressed()
        
        player.key_press()
    
        for event in pygame.event.get():
            # if user  QUIT then the screen will close
            
            if btn_exit.update(pygame.mouse.get_pos(),event): 
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw       
        