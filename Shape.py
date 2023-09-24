import math


# fait la rotation d'un point autour du (0,0)
def rotate(point, angle):
    x = point[0]
    y = point[1]
    
    xp = x*math.cos(angle) - y*math.sin(angle)
    yp = y*math.cos(angle) + x*math.sin(angle)
    ret = [xp,yp]

    return ret
# fait la rotation d'une liste de points
def rotatePoints(points,angle):
    ret = []
    for point in points:
        ret.append(rotate(point,angle))
    return ret


class Shape:
    # 3 variables pour l'instant:
    #   -les points qui composent le polygone
    #   -la position,
    #   -le scale factor
    def __init__(self,_points,_position,_scaleFactor):
        self.points = _points
        self.position = _position
        self.scaleFactor = _scaleFactor


    def rotate(self,angle):
        self.points = rotatePoints(self.points,angle)

    # retourne les points du polygones a leur position et scale up 
    def getVertices(self):
        ret = []
        for point in self.points:
            x = point[0]*self.scaleFactor
            y = point[1]*self.scaleFactor
            posX = self.position[0]
            posY = self.position[1]
            ret.append([x+posX,y+posY])
        return ret
