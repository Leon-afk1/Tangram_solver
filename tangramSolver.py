from functions import *
import pygame
from pygame import gfxdraw
from time import sleep
from Piece import Piece

ROTATION_GAP = 45
SMALL_AREA = 10

bigTriangle1 = Piece(Polygon([(0,0),(400,0),(0,400)]), 0, (0,255,154))
bigTriangle2 = Piece(Polygon([(0,0),(400,0),(0,400)]), 1, (255,154,0))
mediumTriangle = Piece(Polygon([(0,0),(200,0),(0,200)]), 2, (255,0,0))
smallTriangle1 = Piece(Polygon([(0,0),(100,0),(0,100)]), 3, (189,126,0))
smallTriangle2 = Piece(Polygon([(0,0),(100,0),(0,100)]), 4, (189,0,145))
square = Piece(Polygon([(0,0),(100,0),(100,100),(0,100)]), 5, (247,255,0))
trapeze = Piece(Polygon([(0,0),(100,-100),(100,0),(0,100)]), 6, (0,0,204))
trapezeInversed = Piece(Polygon([(0,0),(100,0),(0,100),(-100,100)]), 6, (0,0,204))

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
    shapes = list(multi_shapes.geoms)
    for shape in shapes:
        local_solution = solvePolygon(shape,polys,screen)
        # S'il n'existe pas de solution pour le multipolygon alors rien ne sert de résoudre le reste des polygones
        if local_solution == None:
            return None
        solution.extend(local_solution)
        for sol in local_solution:
            removePiece(polys,sol)
    return solution
    

def solvePolygon(shape,polys,screen):
    solved = False
    solution = []
    if shape.is_empty or shape.area < SMALL_AREA:
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

            displayShape(difference,screen)

            sub_list = createSubList(polygons,selectedPolygon)

            nextPolys = solveTangram(difference,sub_list,screen)

            realPoly = getRealPoly(selectedPolygon,polygons)
            if(nextPolys != None):
                solution.append(selectedPolygon)
                solution.extend(nextPolys)
                solved = True
                break
            else:
                realPoly.Rotate(ROTATION_GAP)
            #remove after all rotations are tested
            if realPoly.revolution:
                polygons = removePiece(polygons,selectedPolygon)
            else:
                realPoly.resetRotation()
                if not realPoly.changeOriginPoint():
                    polygons = removePiece(polygons,selectedPolygon)
    if(not solution):
        return None
    return solution
    

def removePiece(list,piece):
    ret = []
    for p in list:
        if p.id != piece.id:
            ret.append(p)
    return ret

def displayShape(shape,screen):
    if not shape.is_empty and shape.geom_type != "MultiPolygon":
        pygame.gfxdraw.filled_polygon(screen, shape.exterior.coords,(0,0,150))
        pygame.gfxdraw.aapolygon(screen, shape.exterior.coords,(0,0,150))
        pygame.display.update()

def getRealPoly(selected,polys):
    for poly in polys:
        if selected.id == poly.id:
            return poly

def createSubList(polygons,selectedPolygon):
    sub_list = []
    for poly in polygons:
        if selectedPolygon.id != poly.id:
            resetedPoly = poly.copy()
            resetedPoly.reset()
            sub_list.append(resetedPoly)
    return sub_list