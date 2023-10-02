from shapely import *

#   checks if a polygon is going into that place by rotating it and moving it towards the point
def selectPolygon(shape,point,polygons):
    #todo
    return polygons[0]
        
        
#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,polygon):
    transform(polygon.exterior.coords,lambda x: x + point)
    return polygon.covered_by(shape)

