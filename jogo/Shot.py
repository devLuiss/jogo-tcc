import pygame
import math
import random

class  Shot(pygame.sprite.Sprite):
  def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load ("data/pinguin.png") 
        self.image = pygame.transform.scale(self.image, [70, 70])
        self.rect = self.image.get_rect()
        self.speed = 4
        
  def update(self, *args):    
     self.rect.x += self.speed 
        
     if self.rect.left > 840:
           self.kill()   
    