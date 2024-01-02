from Piece import Piece
from shapely import *
import shapely
#test push
#   detects if a polygon is fully into another
#   returns true or false
def fullyIn(polygon,shape):
    #   rouding security
    EPSILON = 0.005
    multishape = MultiPolygon([shape])
    if not shape.is_valid:
        print(shape)
        print("invalid shape")
        return False
    if not multishape.intersection(polygon).is_empty:
        intersection = multishape.intersection(polygon)
        if(abs(intersection.area - polygon.area) <= EPSILON):
            return True
        else:
            return False
    else:
        return False

    

#   checks if a polygon is going into that place by rotating it and moving it towards the point
def selectPolygon(shape,point,polygons):
    #todo
    for polygon in polygons:
        piece = polygon.copy()
        if(polygonIn(shape,point,piece)):
            return piece
    return None
        
        
#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,polygon):
    polygon.moveToPoint(point)
    return fullyIn(polygon.getPoly(),shape)
