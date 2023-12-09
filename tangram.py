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

        self.bigTriangle1 = Polygon([(0, 0), (400, 0), (0, 400)])
        self.squareShape = Polygon([(0, 0), (0, 400 * sqrt(2)), (400 * sqrt(2), 400 * sqrt(2)), (400 * sqrt(2), 0)])
        self.polygon1 = Polygon([(0.5, -0.866025), (1, 0), (0.5, 0.866025), (-0.5, 0.866025), (-1, 0), (-0.5, -0.866025)])
        self.polygon1 = transform(self.polygon1, lambda x: x * 100 + (100, 100))
        self.polygon2 = Polygon([(1, -0.866025), (1.866025, 0), (1, 0.866025), (0.133975, 0)])
        self.polygon2 = transform(self.polygon2, lambda x: x * 100 + (100, 100))
        self.difference = self.polygon2.difference(self.polygon1)
        self.polygons = MultiPolygon([self.squareShape, self.polygon1, self.polygon2, self.difference])

        self.i = 50

    def run(self):
        for poly in self.polygons.geoms:
            #   2 lignes pour ajouter de l'antialiasing, on fill le rectangle et on rajoute les lignes exteieures antialiasé avec la deuxieme ligne
            #   ça existe pas avec pygame un polygone filled antialiased :(
            pygame.gfxdraw.filled_polygon(self.screen, poly.exterior.coords, (self.i, 0, 0))
            pygame.gfxdraw.aapolygon(self.screen, poly.exterior.coords, (self.i, 0, 0))

            self.i += 50

        solution = solveTangram(self.bigTriangle1, tangramPieces, self.screen)
        print(solution)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()