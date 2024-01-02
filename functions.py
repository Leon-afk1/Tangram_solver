import Piece
from shapely import *
import shapely
import math
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
    
    ####################test segment####################

    #polygon = polygons[0]
    #print("polygone de base : " + polygon.string())
    #rotations = get_rotations(shape,point,polygon)
    #list(set(rotations))
    #print("exit get rotations :")
    #print("nb rotations : " + str(len(rotations)))
    #print("polygon apres :" + polygon.string())
    #print("rotation list : ")
    #for eleme in rotations:
    #    print(eleme.string())
    #exit(0)
    ####################################################


    for polygon in polygons:
        rotations = get_rotations(shape,point,polygon)
        #write code to delete duplicates from rotation list
        #print("polygone de base : " + polygon.string())
        rotations = get_rotations(shape,point,polygon)
        list(set(rotations))
        print("exit get rotations :")
        print("nb rotations : " + str(len(rotations)))
        print("polygon apres :" + polygon.string())
        print("rotation list : ")
    
        for poly in rotations:
            
            i +=1
            if(polygonIn(shape,point,poly)):
                return polygon
        
        
        
    return None
        
        
#checks if a polygon is in the shape by moving it on the point
def polygonIn(shape,point,polygon):
    return fullyIn(polygon,shape)


def get_rotations(shape,point,polygon):
    shape_adjacents = getAdjacents(shape)
    res = []
    for points in polygon.poly.exterior.coords:
        polygon.GetTransformed(points)
        for adjacent in shape_adjacents:
            temp = getRotatedAndMirrored(polygon,adjacent)
            print("Adding to rotations : ")
            for elem in temp:
                print(elem.string())
            res.extend(temp)

    return res
    



def getAdjacents(shape):
    return (shape.exterior.coords[-1],shape.exterior.coords[1])


def getRotatedAndMirrored(polygon, point):
    res = polygon.GetRotated(angle_between_segments(polygon.poly.exterior.coords[0],polygon.poly.exterior.coords[1],polygon.poly.exterior.coords[0],point))
    res2 = polygon.GetRotated(angle_between_segments(polygon.poly.exterior.coords[0],polygon.poly.exterior.coords[-1],polygon.poly.exterior.coords[0],point))
    return(res,res2,MirrorImagePolygon(res,polygon.poly.exterior.coords[1]),MirrorImagePolygon(res2,polygon.poly.exterior.coords[-1]))
    



def angle_between_segments(point1, point2, point3, point4):
    
    vector1 = [point2[0] - point1[0], point2[1] - point1[1]]
    vector2 = [point4[0] - point3[0], point4[1] - point3[1]]

    
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    angle_radians = math.atan2(cross_product, dot_product)

    return math.degrees(angle_radians)


def MirrorImagePolygon(polygon,point):
    return polygon.GetChangedPoly(Polygon((symmetrical_points(polygon.poly.exterior.coords[0],point,polygon.poly.exterior.coords))))



def symmetrical_points(segment_start, segment_end, points):
    def dot(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    def scale(v, scalar):
        return (v[0] * scalar, v[1] * scalar)

    def subtract(v1, v2):
        return (v1[0] - v2[0], v1[1] - v2[1])

    def add(v1, v2):
        return (v1[0] + v2[0], v1[1] + v2[1])

    def project(point, line_start, line_end):
        line_vec = subtract(line_end, line_start)
        point_vec = subtract(point, line_start)
        if dot(line_vec,line_vec) != 0:
            t = dot(point_vec, line_vec) / dot(line_vec, line_vec)
        else:
            t=0.5
        
        return add(line_start, scale(line_vec, t))

    def reflect(point, line_start, line_end):
        projection = project(point, line_start, line_end)
        reflection = subtract(scale(projection, 2), point)
        return reflection

    symmetrical_points_list = [reflect(point, segment_start, segment_end) for point in points]
    return symmetrical_points_list
