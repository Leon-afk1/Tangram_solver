from functions import *
import pygame
from pygame import gfxdraw
from time import sleep

bigTriangle1 = Polygon([(0,0),(400,0),(0,400)])
bigTriangle2 = Polygon([(0,0),(400,0),(0,400)])
mediumTriangle = Polygon([(0,0),(200,0),(0,200)])
smallTriangle1 = Polygon([(0,0),(100,0),(0,100)])
smallTriangle2 = Polygon([(0,0),(100,0),(0,100)])
square = Polygon([(0,0),(100,0),(100,100),(0,100)])
trapeze = Polygon([(0,0),(100,-100),(100,0),(0,100)])
trapezeInversed = Polygon([(0,0),(100,0),(0,100),(-100,100)])

tangramPieces = [bigTriangle1,bigTriangle2,mediumTriangle,smallTriangle1,smallTriangle2,square,trapeze,trapezeInversed]


def solveTangram(shape,polys,screen):
    solved = False
    solution = []

    if shape.is_empty:
        return solution
    for shapePoint in shape.exterior.coords:
        polygons = polys.copy()
        while polygons and not solved:
            selectedPolygon = selectPolygon(shape,shapePoint,polygons)

            
            if(selectedPolygon == None):
                break

            polygons.remove(selectedPolygon)
            selectedPolygon = transform(selectedPolygon,lambda x: x + shapePoint)

            ####
            screen.fill((255,255,255))
            pygame.gfxdraw.filled_polygon(screen, selectedPolygon.exterior.coords,(0,100,150))
            pygame.gfxdraw.aapolygon(screen, selectedPolygon.exterior.coords,(0,100,150))
            
            
            ####

            difference = shape.difference(selectedPolygon)
            pygame.gfxdraw.filled_polygon(screen, difference.exterior.coords,(0,0,150))
            pygame.gfxdraw.aapolygon(screen, difference.exterior.coords,(0,0,150))
            pygame.display.update()
            sleep(0.5)
            nextPolys = solveTangram(difference,polygons,screen)
            if(nextPolys != None):
                solution += nextPolys
                solved = True
    if(not solution):
        return None
    return solution