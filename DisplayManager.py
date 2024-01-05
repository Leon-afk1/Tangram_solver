import pygame


class DisplayManager():
    def __init__(self,_pieces,_bgColor = (255,255,255)):
        self.pieces = _pieces.copy()
        self.bgColor = _bgColor
    
    def Update(self,screen):
        screen.fill(self.bgColor)
        for piece in self.pieces:
            print(piece.color)
            piece.display(screen)
        pygame.display.update()