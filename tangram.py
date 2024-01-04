import pygame
from pygame import gfxdraw
from math import sqrt
from shapely import *
from tangramSolver import *
from ShapeGestion import *

class TangramGame:
    def __init__(self, width, height, fond):
        pygame.init()

        # pour la fenetre (osef tier)
        self.background_colour = (255, 255, 255)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tangram')
        self.screen.fill(self.background_colour)
        self.running = True


        if (fond =="multipolygon"):
            bigTriangle1 = Polygon([(50, 50), (150, 50), (50, 150)])
            bigTriangle2 = Polygon([(150, 50), (250, 50), (150, 150)])
            mediumTriangle = Polygon([(250, 50), (250+50*sqrt(2), 50), (250, 50+50*sqrt(2))])
            smallTriangle1 = Polygon([(50, 150), (100, 150), (50, 200)])
            smallTriangle2 = Polygon([(150, 150), (200, 150), (150, 200)])
            square = Polygon([(250, 150), (300, 150), (300, 200), (250, 200)])
            trapeze = Polygon([(150, 250), (200, 200), (200, 250), (150, 300)])
            
            self.testShape = MultiPolygon([bigTriangle1, bigTriangle2, mediumTriangle, smallTriangle1, smallTriangle2, square, trapeze])
        elif (fond =="carre"):
            coté=100*sqrt(2)
            centre_x=( (width - coté) // 2)
            centre_y=( (height - coté) // 2)
            self.testShape = Polygon([(centre_x, centre_y), (centre_x+coté, centre_y), (centre_x+coté, centre_y+coté), (centre_x, centre_y+coté)])
        elif (fond=="chameau"):
            pointfesse_x=251+100*sqrt(2)
            pointfesse_y=59+100*sqrt(2)+100
            self.testShape = Polygon([(251,59),(251+25*sqrt(2),59+25*sqrt(2)),(251+50*sqrt(2),59),(251+50*sqrt(2),59+50*sqrt(2)),(251+100*sqrt(2),59+100*sqrt(2)),
                                      (pointfesse_x,pointfesse_y),(pointfesse_x+50//sqrt(2),pointfesse_y-50//sqrt(2)),(pointfesse_x+50//sqrt(2)+50*sqrt(2),pointfesse_y-50//sqrt(2)),
                                      (pointfesse_x+50*sqrt(2),pointfesse_y),(pointfesse_x,pointfesse_y),(pointfesse_x-100,pointfesse_y),
                                      (251+50*sqrt(2),59+50*sqrt(2)+100*sqrt(2)),(251+50*sqrt(2),59+50*sqrt(2)+100),
                                      (251+50*sqrt(2)-50,59+50*sqrt(2)+50),(251+25*sqrt(2),59+75*sqrt(2)),(251,59+50*sqrt(2))])
            
            
        self.i = 50

    def run(self):
        # solution = solveTangram(self.testShape, tangramPieces, self.screen)
        # print(solution)
        # self.displaySolution(solution)
        # while self.running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             self.running = False

        #     pygame.display.update()
        while self.running:
            self.screen.fill((255,255,255))
            pygame.gfxdraw.filled_polygon(self.screen, self.testShape.exterior.coords,(0,0,150))
            pygame.gfxdraw.aapolygon(self.screen, self.testShape.exterior.coords,(0,0,150))
            pygame.display.update()

    def displaySolution(self,solution):
        self.screen.fill((255,255,255))
        for piece in solution:
            piece.display(self.screen)