from functions import *
import pygame
from Piece import Piece
from EventManager import EventManager
from DisplayManager import DisplayManager
from ShapeGestion import ShapeGestion

class TangramConstructor():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tangram')

        reduction_factor = 1

        # Créez les pièces du Tangram
        bigTriangle1 = Piece(Polygon([(0, 0), (100, 0), (0, 100)]), (0, 255, 154))
        bigTriangle2 = Piece(Polygon([(0, 0), (100, 0), (0, 100)]), (255, 154, 0))
        mediumTriangle = Piece(Polygon([(0, 0), (70.71, 0), (0, 70.71)]), (255, 0, 0))
        smallTriangle1 = Piece(Polygon([(0, 0), (50, 0), (0, 50)]), (189, 126, 0))
        smallTriangle2 = Piece(Polygon([(0, 0), (50, 0), (0, 50)]), (189, 0, 145))
        square = Piece(Polygon([(0, 0), (50, 0), (50, 50), (0, 50)]), (247, 255, 0))
        trapeze = Piece(Polygon([(0, 0), (50, -50), (50, 0), (0, 50)]), (0, 0, 204))

        # Déplacer les pièces à des positions spécifiques
        bigTriangle1.moveToPoint((50, 50))
        bigTriangle2.moveToPoint((150, 50))
        mediumTriangle.moveToPoint((250, 50))
        smallTriangle1.moveToPoint((50, 150))
        smallTriangle2.moveToPoint((150, 150))
        square.moveToPoint((250, 150))
        trapeze.moveToPoint((150, 250))

        tangramPieces = [bigTriangle1, bigTriangle2, mediumTriangle, smallTriangle1, smallTriangle2, square, trapeze]

        # Ajustez la taille de chaque pièce
        for piece in tangramPieces:
            piece.scale(reduction_factor)


        self.pieces = tangramPieces

    def run(self):
        
        self.pieces=ShapeGestion.importFile("res/data.json")
        
        eventManager = EventManager(self.pieces)
        displayManager = DisplayManager(self.pieces)

        while eventManager.running:
            eventManager.Event()
            displayManager.Update(self.screen)
            
        ShapeGestion.saveFile("res/data.json", self.pieces)
