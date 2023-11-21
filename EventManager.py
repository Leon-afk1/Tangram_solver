import pygame
from shapely import *

class EventManager():
    def __init__(self,_pieces):
        self.pieces = _pieces
        self.running = True
        self.pieceHeld = None

    def Event(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                    break
                case pygame.MOUSEBUTTONDOWN:
                    self.OnMouseDown()
                case pygame.MOUSEBUTTONUP:
                    self.OnMouseUp()
        if(self.pieceHeld != None):
            self.OnGrab()

    def OnMouseDown(self):
        mousePos = pygame.mouse.get_pos()
        mousePosPoint = Point(mousePos)
        for piece in self.pieces:
            if(mousePosPoint.within(piece.poly)):
                self.pieceHeld = piece
                piece.OnMouseDown(mousePos)
    
    def OnMouseUp(self):
        if(self.pieceHeld != None):
            self.pieceHeld.OnMouseUp()
        self.pieceHeld = None

    def OnGrab(self):
        otherPieces = self.pieces.copy()
        otherPieces.remove(self.pieceHeld)
        self.pieceHeld.OnGrab(pygame.mouse.get_pos(),otherPieces)
