from functions import *
import pygame
from pygame import gfxdraw
from time import sleep
from Piece import Piece

bigTriangle1 = Piece(Polygon([(0,0),(400,0),(0,400)]),(0,255,154))
bigTriangle2 = Piece(Polygon([(0,0),(400,0),(0,400)]),(255,154,0))
mediumTriangle = Piece(Polygon([(0,0),(200,0),(0,200)]),(255,0,0))
smallTriangle1 = Piece(Polygon([(0,0),(100,0),(0,100)]),(189,126,0))
smallTriangle2 = Piece(Polygon([(0,0),(100,0),(0,100)]),(189,0,145))
square = Piece(Polygon([(0,0),(100,0),(100,100),(0,100)]),(247,255,0))
trapeze = Piece(Polygon([(0,0),(100,-100),(100,0),(0,100)]),(0,0,204))
trapezeInversed = Piece(Polygon([(0,0),(100,0),(0,100),(-100,100)]),(0,0,204))

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
            selectedPolygon.polygon = transform(selectedPolygon.polygon,lambda x: x + shapePoint)

            ####
            screen.fill((255,255,255))
            selectedPolygon.display(screen)
            
            
            ####

            difference = shape.difference(selectedPolygon.polygon)
            print("oue")
            pygame.gfxdraw.filled_polygon(screen, difference.exterior.coords,(0,0,150))
            pygame.gfxdraw.aapolygon(screen, difference.exterior.coords,(0,0,150))
            pygame.display.update()
            sleep(0.5)
            print("oue")
            nextPolys = solveTangram(difference,polygons,screen)
            print("oue")
            if(nextPolys != None):
                solution += nextPolys
                solved = True
    if(not solution):
        return None
    return solution