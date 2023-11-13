import pygame
import numpy as np

class grand_triangle1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load('gros_triangle1.png').convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class grand_triangle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('gros_triangle2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = self.create_mask()

    def create_mask(self):
        x = 300 
        y = self.rect.height - 10 
        mask = pygame.mask.from_surface(self.image)
        mask_rect = mask.get_rect()
        mask_rect.topleft = (x, y)
        return mask

    def update(self):
        self.update_mask() 
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        
    def update_mask(self):
        self.mask = self.create_mask()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

        

