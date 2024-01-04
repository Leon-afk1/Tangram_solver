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
        elif (fond=="chat"):
            pointfesse_x=251+100*sqrt(2)
            pointfesse_y=59+100*sqrt(2)+100
            self.testShape = Polygon([(251,59),(251+25*sqrt(2),59+25*sqrt(2)),(251+50*sqrt(2),59),(251+50*sqrt(2),59+50*sqrt(2)),(251+100*sqrt(2),59+100*sqrt(2)),
                                      (pointfesse_x,pointfesse_y),(pointfesse_x+50//sqrt(2),pointfesse_y-50//sqrt(2)),(pointfesse_x+50//sqrt(2)+50*sqrt(2),pointfesse_y-50//sqrt(2)),
                                      (pointfesse_x+50*sqrt(2),pointfesse_y),(pointfesse_x,pointfesse_y),(pointfesse_x-100,pointfesse_y),
                                      (251+50*sqrt(2),59+50*sqrt(2)+100*sqrt(2)),(251+50*sqrt(2),59+50*sqrt(2)+100),
                                      (251+50*sqrt(2)-50,59+50*sqrt(2)+50),(251+25*sqrt(2),59+75*sqrt(2)),(251,59+50*sqrt(2))])
        elif (fond=="lapin"):
            self.testShape = Polygon([(295,140),(325,140),(375,90),(425,90),(375,140),(345,140),(345,165),(445,265),(445,365),(445-50*sqrt(2),365),
                                      (445-50*sqrt(2)-sqrt(1250),365-25*sqrt(2)),(445-50*sqrt(2),365-50*sqrt(2)),(345,265),(345,265+25*sqrt(2)),(345-25*sqrt(2),265),(345,265-25*sqrt(2)),
                                      (345,190),(295,190)])
        elif (fond=="ours"):
            pointJambe_x=255-50*sqrt(2)+25*sqrt(2)
            pointJambe_y=155+50*sqrt(2)+25*sqrt(2)
            self.testShape = Polygon([(255,155),(405,155),(455,205),(355,205),(355,155+50*sqrt(2)),(405,205+50*sqrt(2)),(355,205+50*sqrt(2)),(305,155+50*sqrt(2)),
                                      (355-50*sqrt(2),155+50*sqrt(2)),(255,255),(255,155+100*sqrt(2)),(pointJambe_x+50,pointJambe_y+50),
                                      (pointJambe_x,pointJambe_y+50),(pointJambe_x,pointJambe_y),(255-50*sqrt(2),155+50*sqrt(2))])
        else:
            shape = ShapeGestion()
            exterior_polygon = shape.importShapeFile("res/data.json")
            self.testShape = exterior_polygon




    def run(self):
        solution = solveTangram(self.testShape, tangramPieces, self.screen)
        print(solution)
        self.displaySolution(solution)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
        # while self.running:
        #     self.screen.fill((255,255,255))
        #     pygame.gfxdraw.filled_polygon(self.screen, self.testShape.exterior.coords,(0,0,150))
        #     pygame.gfxdraw.aapolygon(self.screen, self.testShape.exterior.coords,(0,0,150))
        #     pygame.display.update()
        #     for event in pygame.event.get():
        #         match event.type:
        #             case pygame.QUIT:
        #                 self.running = False
        #                 break

    def displaySolution(self,solution):
        self.screen.fill((255,255,255))
        for piece in solution:
            piece.display(self.screen)