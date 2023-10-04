from shapely import *
#test push
#   detects if a polygon is fully into another
#   returns true or false
def fullyIn(polygon,shape):
    #   rouding security
    EPSILON = 0.005
    intersection = shape.intersection(polygon)

    if(abs(intersection.area - polygon.area) <= EPSILON):
        print(polygon)
        return True
    else:
        return False
    

#   checks if a polygon is going into that place by rotating it and moving it towards the point
def selectPolygon(shape,point,polygons):
    #todo
    for polygon in polygons:
        if(polygonIn(shape,point,polygon)):
            return polygon
    return None
        
        
#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,polygon):

    polygon = transform(polygon,lambda x: x + point)
    return fullyIn(polygon,shape)
