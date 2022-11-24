import pygame
import random
from player import player
from Windows import Windows
from Shot import Shot

pygame.init()
#inicializando o paygame e criando a janela.

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Linux respect")

#Grroup objects
objectGroup = pygame.sprite.Group()
WindowsGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()




#Background!!
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/fundo.jfif")
bg.image = pygame.transform.scale(bg.image,[840, 480])
bg.rect = bg.image.get_rect()
player = player (objectGroup)

#music
pygame.mixer.music.load("data/musica2.wav")
pygame.mixer.music.play(-1)


#sounds
shoot = pygame.mixer.Sound("data/shoot.wav")


gameLoop = True
gameover = False
timer = 20
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_SPACE and not gameover: 
                    shoot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center  
       
        # Update logiv:
        if not gameover:
            objectGroup.update()
            
            timer += 1 
            if timer > 30:
                timer = 0
                if random.random() <0.5:
                    newWindows = Windows(objectGroup, WindowsGroup)

            collisions = pygame.sprite.spritecollide(player, WindowsGroup, False, pygame.sprite.collide_mask)  
            
            if collisions:
                print ("Game over!")
                gameover = True
                
            hits = pygame.sprite.groupcollide(shotGroup, WindowsGroup, True, True, pygame.sprite.collide_mask)    
            
            
        # Update and Draw 
        display.fill([46, 46, 46])
        objectGroup.draw(display)
        pygame.display.update()