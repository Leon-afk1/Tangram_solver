from functions import *
import pygame
from pygame import gfxdraw
from time import sleep
from Piece import Piece
from math import sqrt

reduction_factor = 1

# Créez les pièces du Tangram
bigTriangle1 = Piece(Polygon([(0, 0), (100, 0), (0, 100)]), (0, 255, 154))
bigTriangle2 = Piece(Polygon([(0, 0), (100, 0), (0, 100)]), (255, 154, 0))
mediumTriangle = Piece(Polygon([(0, 0), (50*sqrt(2), 0), (0, 50*sqrt(2))]), (255, 0, 0))
smallTriangle1 = Piece(Polygon([(0, 0), (50, 0), (0, 50)]), (189, 126, 0))
smallTriangle2 = Piece(Polygon([(0, 0), (50, 0), (0, 50)]), (189, 0, 145))
square = Piece(Polygon([(0, 0), (50, 0), (50, 50), (0, 50)]), (247, 255, 0))
trapeze = Piece(Polygon([(0, 0), (50, -50), (50, 0), (0, 50)]), (0, 0, 204))
trapezeInversed = Piece(Polygon([(0, 0), (50, 50), (50, 0), (0, -50)]), (0, 0, 204))

tangramPieces = [bigTriangle1,bigTriangle2,mediumTriangle,smallTriangle1,smallTriangle2,square,trapeze,trapezeInversed]

# Ajustez la taille de chaque pièce
for piece in tangramPieces:
    piece.scale(reduction_factor)


def solveTangram(shape,polys,screen):
    solution = []
    if shape.geom_type == "MultiPolygon":
        solution = solveMultipolygon(shape,polys,screen)
    else:
        solution = solvePolygon(shape,polys,screen)
    return solution


def solveMultipolygon(multi_shapes,polys,screen):
    solution = []
    polygons = polys.copy()
    shapes = list(multi_shapes.geoms)
    for shape in shapes:
        local_solution = solvePolygon(shape,polygons,screen)
        # S'il n'existe pas de solution pour le multipolygon alors rien ne sert de résoudre le reste des polygones
        if local_solution == None:
            return None
        solution.extend(local_solution)
        for sol in local_solution:
            polygons.remove(sol)
    return solution
    

def solvePolygon(shape,polys,screen):
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
            pygame.display.update()
            ####

            difference = shape.difference(selectedPolygon.getPoly())
            if not difference.is_empty and difference.geom_type != "MultiPolygon":
                pygame.gfxdraw.filled_polygon(screen, difference.exterior.coords,(0,0,150))
                pygame.gfxdraw.aapolygon(screen, difference.exterior.coords,(0,0,150))
                pygame.display.update()
                sleep(1)
            nextPolys = solveTangram(difference,polygons,screen)
            if(nextPolys != None):
                solution.append(selectedPolygon)
                solution += nextPolys
                solved = True
    if(not solution):
        return None
    return solution
    