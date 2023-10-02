from functions import *

bigTriangle1 = ([(0,0),(400,0),(0,400)])
bigTriangle2 = ([(0,0),(400,0),(0,400)])
mediumTriangle = ([(0,0),(200,0),(0,200)])
smallTriangle1 = ([(0,0),(100,0),(0,100)])
smallTriangle2 = ([(0,0),(100,0),(0,100)])
square = ([(0,0),(100,0),(100,100),(0,100)])
trapeze = ([(0,0),(100,-100),(100,0),(0,100)])
trapezeInversed = ([(0,0),(100,0),(0,100),(-100,100)])

polygons = [bigTriangle1,bigTriangle2,mediumTriangle,smallTriangle1,smallTriangle2,square,trapeze,trapezeInversed]


def solveTangram(shape,polys):
    solved = False
    polygons = polys.copy()
    solution = []

    if shape.is_empty:
        return solution
    for shapePoint in shape.exterior.coords:
        while polygons and not solved:
            selectedPolygon = selectPolygon(shape,shapePoint,polygons)
            if(selectedPolygon == None):
                break
            difference = shape.difference(selectedPolygon)
            polygons.remove(selectedPolygon)
            nextPolys = solveTangram(difference,polygons)
            if(nextPolys != None):
                solution += nextPolys
                solved = True
    if(not solution):
        return None
    return solution