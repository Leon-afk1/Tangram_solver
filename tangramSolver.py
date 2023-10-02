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
    polygons = polys.copy()

    for shapePoint in shape.exterior.coords:
        selectedPolygon = selectPolygon(shape,shapePoint,polygons)
        if(selectedPolygon == None):
            return None
        difference = shape.difference(selectedPolygon)
        polygons.remove(selectedPolygon)
        solveTangram(shape,polygons)


