from shapely import *
import shapely
#test push
#   detects if a polygon is fully into another
#   returns true or false
def fullyIn(polygon,shape):
    #   rouding security
    EPSILON = 0.005
    poly = Polygon(polygon.getPoly())
    if type(shape.intersection(poly)) == shapely.geometry.polygon.Polygon and not shape.intersection(poly).is_empty:
        intersection = shape.intersection(poly)
        if(abs(intersection.area - poly.area) <= EPSILON):
            return True
        else:
            return False
    else:
        return False

    

#   checks if a polygon is going into that place by rotating it and moving it towards the point
def selectPolygon(shape,point,polygons):
    #todo
    i = 0
    for polygon in polygons:
        print(i)
        i +=1
        if(polygonIn(shape,point,polygon)):
            return polygon
    return None
        
        
#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,polygon):
    polygon.moveToPoint(point)
    return fullyIn(polygon,shape)
