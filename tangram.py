import pygame
from pygame import gfxdraw
from math import sqrt
from shapely import *
from tangramSolver import *

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

        bigTriangle1 = Polygon([(0, 0), (400, 0), (0, 400)])
        mediumTriangleTest = Polygon([(400,400),(600,400),(400,600)])

        self.squareShape = Polygon([(0, 0), (0, 400 * sqrt(2)), (400 * sqrt(2), 400 * sqrt(2)), (400 * sqrt(2), 0)])
        self.squareShapeOffseted = Polygon([(100, 100), (100,100+ 400 * sqrt(2)), (100 + 400 * sqrt(2), 100 + 400 * sqrt(2)), (100 + 400 * sqrt(2), 100)])
        self.testShape = MultiPolygon([bigTriangle1,mediumTriangleTest])

        self.i = 50

    def run(self):
        solution = solveTangram(self.squareShape, tangramPieces, self.screen)
        print(solution)
        self.displaySolution(solution)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
    
    def displaySolution(self,solution):
        self.screen.fill((255,255,255))
        if solution == None:
            print("No solution")
            return
        for piece in solution:
            piece.display(self.screen)