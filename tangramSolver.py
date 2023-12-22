from functions import *
import pygame
from pygame import gfxdraw
from time import sleep
from Piece import Piece

bigTriangle1 = Piece(Polygon([(0,0),(200,0),(0,200)]), (0,255,154))
bigTriangle2 = Piece(Polygon([(0,0),(200,0),(0,200)]), (255,154,0))
mediumTriangle = Piece(Polygon([(0,0),(100,0),(0,100)]), (255,0,0))
smallTriangle1 = Piece(Polygon([(0,0),(50,0),(0,50)]), (189,126,0))
smallTriangle2 = Piece(Polygon([(0,0),(50,0),(0,50)]), (189,0,145))
square = Piece(Polygon([(0,0),(50,0),(50,50),(0,50)]), (247,255,0))
trapeze = Piece(Polygon([(0,0),(50,-50),(50,0),(0,50)]), (0,0,204))
trapezeInversed = Piece(Polygon([(0,0),(50,0),(0,50),(-50,50)]), (0,0,204))

tangramPieces = [bigTriangle1, bigTriangle2, mediumTriangle, smallTriangle1, smallTriangle2, square, trapeze, trapezeInversed]


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
            selectedPolygon.moveToPoint(shapePoint)

            ####
            screen.fill((255,255,255))
            selectedPolygon.display(screen)
            
            
            ####
            difference = shape.difference(selectedPolygon.getPoly())
            print(difference)
            if not difference.is_empty:
                pygame.gfxdraw.filled_polygon(screen, difference.exterior.coords,(0,0,150))
                pygame.gfxdraw.aapolygon(screen, difference.exterior.coords,(0,0,150))
                pygame.display.update()
                sleep(0.1)
            nextPolys = solveTangram(difference,polygons,screen)
            print(nextPolys)
            if(nextPolys != None):
                solution.append(selectedPolygon.getPoly())
                solution += nextPolys
                solved = True
    if(not solution):
        return None
    return solution