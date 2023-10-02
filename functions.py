from shapely import *

#   detects if a polygon is fully into another
#   returns true or false
def fullyIn(polygon,shape):
    intersection = shape.intersection(polygon)
    if(intersection.area == polygon.area):
        return True
    else:
        return False

#   checks if a polygon is going into that place by rotating it and moving it towards the point
def selectPolygon(shape,point,polygons):
    return polygons[0]
        
        
#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,polygon):
    transform(polygon.exterior.coords,lambda x: x + point)
    return fullyIn(polygon,shape)

