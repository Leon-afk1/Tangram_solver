import pygame
from forme import *

pygame.init()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

        self.grand_triangle1_ = grand_triangle1(100, 100)
        self.grand_triangle2_ = grand_triangle2()

        self.triangle_group = pygame.sprite.Group()
        self.piece_select = pygame.sprite.Group()

        self.triangle_group.add(self.grand_triangle1_)
        self.piece_select.add(self.grand_triangle2_)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.grand_triangle1_.rotate(5)
            elif key[pygame.K_RIGHT]:
                self.grand_triangle1_.rotate(-5)
                
    def display(self):
        self.screen.fill("white")
        if pygame.sprite.spritecollide(self.piece_select.sprites()[0], self.triangle_group, False, pygame.sprite.collide_mask):
            print("collision")
        else:
            print("no collision")
        self.grand_triangle1_.draw(self.screen)
        self.grand_triangle2_.update()
        self.triangle_group.update()
        self.piece_select.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.display()
            self.clock.tick(60)

screen = pygame.display.set_mode((1080, 720))
game = Game(screen)
game.run()

pygame.quit()

