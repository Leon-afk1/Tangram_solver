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
    print("Entré dans la fonction solveTangram")
    if shape.is_empty:
        return solution
    for shapePoint in shape.exterior.coords:
        polygons = polys.copy()
        print(shapePoint)
        while polygons and not solved:
            selectedPolygon = selectPolygon(shape,shapePoint,polygons)
            
            if(selectedPolygon == None):
                print("no polygon selected")
                break

            polygons.remove(selectedPolygon)
            selectedPolygon.moveToPoint(shapePoint)

            ####
            screen.fill((255,255,255))
            selectedPolygon.display(screen)
            
            
            ####
            print("selectedPolygon: ",selectedPolygon.getPoly())
            difference = shape.difference(selectedPolygon.getPoly())
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