from functions import *
import pygame
from pygame import gfxdraw
from time import sleep
from Piece import Piece
from math import sqrt

reduction_factor = 1

#   rouding security
EPSILON = 1
ROTATION_GAP = 45
SMALL_AREA = 10

already_tested = []

# Créez les pièces du Tangram
bigTriangle1 = Piece(Polygon([(0, 0), (100, 0), (0, 100)]), 0, (0, 255, 154))
bigTriangle2 = Piece(Polygon([(0, 0), (100, 0), (0, 100)]), 1, (255, 154, 0))
mediumTriangle = Piece(Polygon([(0, 0), (50*sqrt(2), 0), (0, 50*sqrt(2))]), 2, (255, 0, 0))
smallTriangle1 = Piece(Polygon([(0, 0), (50, 0), (0, 50)]), 3, (189, 126, 0))
smallTriangle2 = Piece(Polygon([(0, 0), (50, 0), (0, 50)]), 4, (189, 0, 145))
square = Piece(Polygon([(0, 0), (50, 0), (50, 50), (0, 50)]), 5, (247, 255, 0))
trapeze = Piece(Polygon([(0, 0), (50, -50), (50, 0), (0, 50)]), 6, (0, 0, 204))
trapezeInversed = Piece(Polygon([(0, 0), (50, 50), (50, 0), (0, -50)]), 6, (0, 0, 204))

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
    shapes = list(multi_shapes.geoms)
    for shape in shapes:
        local_solution = solvePolygon(shape,polys,screen)
        # S'il n'existe pas de solution pour le multipolygon alors rien ne sert de résoudre le reste des polygones
        if local_solution == None:
            return None
        solution.extend(local_solution)
        for sol in local_solution:
            polys = removePiece(polys,sol)
    return solution
    

def solvePolygon(shape,polys,screen):
    solution = []

    if shape.is_empty or shape.area < SMALL_AREA:
        displayShape(shape,screen)
        return solution
    for shapePoint in shape.exterior.coords:
        polygons = polys.copy()
        while polygons:
            # sleep(1)
            selectedPolygonReal,polygons = selectPolygon(shape,shapePoint,polygons)

            if(selectedPolygonReal == None):
                break
            selectedPolygon = selectedPolygonReal.copy()
            selectedPolygonReal.nextPosition(ROTATION_GAP)
            selectedPolygon.moveToPoint(shapePoint)

            # ####
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
            
            difference = roundShape(difference,2)
            displayShape(difference,screen)

            # use the poly list because polygons list delete pieces as they don't fit
            sub_list = createSubList(polys,selectedPolygon)
            nextPolys = None
            nextPolys = solveTangram(difference,sub_list,screen)

            if(nextPolys != None):
                solution.append(selectedPolygon)
                solution.extend(nextPolys)
                
                return solution
    return None
    

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
    # print("create sub_list without n°" + str(selectedPolygon.id))
    sub_list = []
    for poly in polygons:
        if selectedPolygon.id != poly.id:
            resetedPoly = poly.copy()
            resetedPoly.reset()
            sub_list.append(resetedPoly)
    return sub_list

    
#   checks if a polygon is going into that place by rotating it and moving it towards the point
def selectPolygon(shape,point,polygons):
    selectedPolygon = None
    new_polygon_list = []
    found = False

    for p in polygons:
        if found:
            new_polygon_list.append(p)
        else:
            found = checkPiece(shape,point,p)
            if found:
                selectedPolygon = p

    return (selectedPolygon,new_polygon_list)
    
        

def checkPiece(shape,point,piece):
    while not piece.allPositionUsed():
        if(piece.id == 0):
            print("rotation angle: "+str(piece.rotation_angle),", point : " + str(piece.origin_point))
        if polygonIn(shape,point,piece):
            return True
        piece.nextPosition(ROTATION_GAP)
    return False

#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,piece):
    piece.moveToPoint(point)
    return fullyIn(piece.getPoly(),shape)

#   detects if a polygon is fully into another
#   returns true or false
def fullyIn(polygon,shape):

    multishape = MultiPolygon([shape])
    if not shape.is_valid:
        make_valid(shape)
        if not shape.is_valid:
            print("error")
    if not multishape.intersection(polygon).is_empty:
        intersection = multishape.intersection(polygon)
        if(abs(intersection.area - polygon.area) <= EPSILON):
            return True
        else:
            return False
    else:
        return False


def roundShape(shape,digit):
    if shape.geom_type == "MultiPolygon":
        shapes = list(shape.geoms)
        for poly in shapes:
            poly = roundPoly(poly,digit)
    else:
        shape = roundPoly(shape,digit)
    return shape
    
def roundPoly(poly,digit):
    if poly.area < SMALL_AREA:
        return Polygon()
    coords = poly.exterior.coords[:]
    for i in range(len(coords)):
        x,y = coords[i]
        coords[i] = (round(x,digit),round(y,digit))
    poly = Polygon(coords)
    make_valid(poly)
    return poly

def checkTested(shape,polygons):
    ids = []
    for poly in polygons:
        if poly.id == 1:
            ids.append(0)
        if poly.id == 4:
            ids.append(3)
        else:
            ids.append(poly.id)
    ids.sort()
    for tested in already_tested:
        if tested[0].equals_exact(shape, SMALL_AREA) and ids == tested[1]:
            print("avoided")
            return True
    return False

def saveTested(shape,polygons):
    ids = []
    for poly in polygons:
        if poly.id == 1:
            ids.append(0)
        if poly.id == 4:
            ids.append(3)
        else:
            ids.append(poly.id)
    ids.sort()
    already_tested.append([shape,ids])