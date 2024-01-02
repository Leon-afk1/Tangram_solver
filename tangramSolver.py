from functions import *
import pygame
from pygame import gfxdraw
from time import sleep
from Piece import Piece

ROTATION_GAP = 90

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
            print(sol)
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
            
            selectedPolygon.moveToPoint(shapePoint)

            ####
            screen.fill((255,255,255))
            selectedPolygon.display(screen)
            ####

            difference = shape.difference(selectedPolygon.getPoly())
            #####   bug Fix ######
            if difference.geom_type == "GeometryCollection":
                for geom in difference.geoms:
                    if(geom.geom_type in ["MultiPolygon","Polygon"]):
                        difference = geom
                        break

            if not difference.is_empty and difference.geom_type != "MultiPolygon":
                pygame.gfxdraw.filled_polygon(screen, difference.exterior.coords,(0,0,150))
                pygame.gfxdraw.aapolygon(screen, difference.exterior.coords,(0,0,150))
                pygame.display.update()
                #sleep(0.1)
            nextPolys = solveTangram(difference,polygons,screen)
            if(nextPolys != None):
                solution.append(selectedPolygon)
                solution += nextPolys
                solved = True
            else:
                selectedPolygon.Rotate(ROTATION_GAP)
            #remove after all rotations are tested
            if selectedPolygon.revolution:
                polygons.remove(selectedPolygon)
    if(not solution):
        return None
    return solution
    