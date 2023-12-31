import pygame
from pygame import gfxdraw
from math import sqrt
from shapely import *
from tangramSolver import *
from ShapeGestion import *

class TangramGame:
    def __init__(self, width, height):
        pygame.init()

        # pour la fenetre (osef tier)
        self.background_colour = (255, 255, 255)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tangram')
        self.screen.fill(self.background_colour)
        self.running = True

        # Créez les pièces du Tangram
        bigTriangle1 = Polygon([(50, 50), (150, 50), (50, 150)])
        bigTriangle2 = Polygon([(150, 50), (250, 50), (150, 150)])
        mediumTriangle = Polygon([(250, 50), (320.71, 50), (250, 120.71)])
        smallTriangle1 = Polygon([(50, 150), (100, 150), (50, 200)])
        smallTriangle2 = Polygon([(150, 150), (200, 150), (150, 200)])
        square = Polygon([(250, 150), (300, 150), (300, 200), (250, 200)])
        trapeze = Polygon([(150, 250), (200, 200), (200, 250), (150, 300)])
        
        self.testShape = MultiPolygon([bigTriangle1, bigTriangle2, mediumTriangle, smallTriangle1, smallTriangle2, square, trapeze])
        # self.testShape = MultiPolygon([bigTriangle1, bigTriangle2, mediumTriangle, smallTriangle1, smallTriangle2, square])

        self.i = 50

    def run(self):
        solution = solveTangram(self.testShape, tangramPieces, self.screen)
        print(solution)
        self.displaySolution(solution)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
    
    def displaySolution(self,solution):
        self.screen.fill((255,255,255))
        for piece in solution:
            piece.display(self.screen)