from shapely import *
import pygame
from pygame import gfxdraw

class Piece():
    def __init__(self,_polygon,_color,_coord=Point((0,0))):
        self.color = _color
        self.poly = Polygon(_polygon)
        self.coord = _coord

    def display(self,screen):
        pygame.gfxdraw.filled_polygon(screen, self.poly.exterior.coords,self.color)
        pygame.gfxdraw.aapolygon(screen, self.poly.exterior.coords,self.color)

    def getPoly(self):
        return self.poly
    
    def setPoly(self,newPoly):
        self.poly = Polygon(newPoly)

    def moveToPoint(self,point):
        x,y = point
        coords = self.poly.exterior.coords[:]
        for i in range(len(coords)):
            cx,cy = coords[i]
            coords[i] = (cx + (x - self.coord.x), cy + (y - self.coord.y))
        self.poly = Polygon(coords)
        self.coord = Point(point)
