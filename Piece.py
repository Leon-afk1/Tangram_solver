from shapely import *
import pygame
from pygame import gfxdraw
import math
from shapely.affinity import rotate

class Piece():
    def __init__(self,_polygon,_id = 0,_color = (255,255,0), _coord=Point((0,0))):
        self.color = _color
        self.original_poly = Polygon(_polygon)
        self.poly = Polygon(_polygon)
        self.coord = Point(_coord)
        self.grabOffset = self.coord
        self.rotation_angle = 0.0
        self.revolution = False
        self.id = _id
        self.origin_point = 0

    def copy(self):
        copied = Piece(self.getPoly(),self.id,self.color,self.getCoord())
        copied.grabOffset = self.grabOffset
        copied.rotation_angle = self.rotation_angle
        copied.revolution = self.revolution
        return copied
    
    def roundPoly(self):
        coords = self.poly.exterior.coords[:]
        for i in range(len(coords)):
            x,y = coords[i]
            coords[i] = (round(x,2),round(y,2))
        self.poly = Polygon(coords)

    def resetRotation(self):
        self.rotation_angle = 0
        self.revolution = False

    def reset(self):
        self.poly = Polygon(self.original_poly)
        self.resetRotation()
        #   reset origin point of piece
        self.origin_point = 0
        self.coord = Point(self.poly.exterior.coords[0])

    def getPoly(self):
        return Polygon(self.poly)
    
    def setPoly(self, newPoly):
        self.poly = Polygon(newPoly)
    
    def getCoord(self):
        return Point(self.coord)

    def moveToPoint(self, point):
        x, y = point
        coords = self.poly.exterior.coords[:]
        for i in range(len(coords)):
            cx, cy = coords[i]
            cx, cy = coords[i]
            coords[i] = (cx + (x - self.coord.x), cy + (y - self.coord.y))
        self.poly = Polygon(coords)
        self.coord = Point(point)

    def allPositionUsed(self):
        return self.allPointUsed() and self.revolution

    def nextPosition(self,angle):
        if self.revolution:
            self.resetRotation()
            if not self.allPointUsed():
                self.changeOriginPoint(self.origin_point+1)
        else:
            self.Rotate(angle)

    def Rotate(self, angle):
        self.rotation_angle += angle
        if self.rotation_angle >= 360:
            self.revolution = True 
            self.rotation_angle -= 360
        self.poly = rotate(self.poly, angle, origin=self.coord)
        # self.roundPoly()

    def changeOriginPoint(self, new_origin_point):
        if new_origin_point + 1 < len(self.poly.exterior.coords):
            last_origin = self.poly.exterior.coords[self.origin_point]
            self.origin_point = new_origin_point
            self.coord = Point(self.poly.exterior.coords[self.origin_point])
            self.moveToPoint(last_origin)
            
    def allPointUsed(self):
        if self.origin_point + 2 >= len(self.poly.exterior.coords):
            return True
        return False

    #   Shape Creator   #
    def display(self, screen):
        pygame.gfxdraw.filled_polygon(screen, self.poly.exterior.coords, self.color)
        pygame.gfxdraw.aapolygon(screen, self.poly.exterior.coords, self.color)

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
 
    def scale(self, factor):
        self.poly = Polygon([(x * factor, y * factor) for x, y in self.poly.exterior.coords])

    def rotate(self, angle,pieces):
        self.rotation_angle += angle
        if self.CollisionCheck(pieces):
            self.rotation_angle -= angle
