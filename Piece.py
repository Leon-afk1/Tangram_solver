from shapely import *
import pygame
from pygame import gfxdraw
import math
from shapely.affinity import rotate

class Piece():
    def __init__(self,_polygon,_color, _coord=Point((0,0))):
        self.color = _color
        self.poly = Polygon(_polygon)
        self.coord = Point(_coord)
        self.grabOffset = self.coord

    def display(self, screen):
        #rotated_poly = rotate(self.poly, self.rotation_angle, origin=self.coord)
        pygame.gfxdraw.filled_polygon(screen, self.poly.exterior.coords, self.color)
        pygame.gfxdraw.aapolygon(screen, self.poly.exterior.coords, self.color)

    def getPoly(self):
        return self.poly
    
    def setPoly(self, newPoly):
        self.poly = Polygon(newPoly)
        return self

    def moveToPoint(self, point):
        x, y = point
        coords = self.poly.exterior.coords[:]
        for i in range(len(coords)):
            cx, cy = coords[i]
            coords[i] = (cx + (x - self.coord.x), cy + (y - self.coord.y))
        self.poly = Polygon(coords)
        self.coord = Point(point)

    def rotate(self, angle,pieces):
        self.rotation_angle += angle
        if self.CollisionCheck(pieces):
            self.rotation_angle -= angle
        return self

        

    def setOffset(self, mousePos):
        x, y = mousePos
        x -= self.coord.x
        y -= self.coord.y
        self.grabOffset = Point(x, y)

    def OnMouseDown(self, mousePos):
        print("mouseDown")
        self.setOffset(mousePos)

    def OnMouseUp(self):
        print("mouseUp")

    def OnGrab(self, mousePos, pieces):
        mouseX, mouseY = mousePos
        newX = mouseX - self.grabOffset.x
        newY = mouseY - self.grabOffset.y

        oldX = self.coord.x
        oldY = self.coord.y
        self.moveToPoint((newX, newY))
        if self.CollisionCheck(pieces):
            self.moveToPoint((oldX, oldY))
            self.setOffset(mousePos)

    def CollisionCheck(self, pieces):
        rotated_poly = rotate(self.poly, self.rotation_angle, origin=self.coord)
        buffered_poly = rotated_poly.buffer(1e-2)  # Ajustez la valeur du tampon selon vos besoins

        for piece in pieces:
            if buffered_poly.intersects(piece.poly):
                return True
    
    def GetRotated(self,angle):
        return Piece(Polygon(RotatePoint(point,angle) for point in self.poly.exterior.coords),self.color,self.coord)

    def GetChangedPoly(self,polygon):
        return Piece(polygon,self.color,self.coord)

    def Rotate(self, angle):
        self.poly = Polygon(RotatePoint(point,angle) for point in self.poly.exterior.coords)
        return self
    

    def Transform(self,anchor):
        self.poly = Polygon(Subtract(point,anchor) for point in self.poly.exterior.coords)
        
    def GetTransformed(self,anchor):
        return Piece(Polygon(Subtract(point,anchor) for point in self.poly.exterior.coords),self.color,self.coord)

    def string(self):
        listcoords = [str(coord) for coord in self.poly.exterior.coords]
        return "Color : " + str(self.color) + "\n" + "Shape : " + str(listcoords)   + "\n" + "Coords : " + str(self.coord) + "\n"



def Subtract(point1,point2):
    return Point(point1[0]-point2[0],point1[1]-point2[1])

def RotatePoint(point, angle):
    rad_angle = math.radians(angle)
    return(Point(point[0] * math.cos(rad_angle) - point[1] * math.sin(rad_angle), point[0] * math.sin(rad_angle) - point[1] * math.cos(rad_angle)))
    
