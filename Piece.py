from shapely import *
import pygame
from pygame import gfxdraw

class Piece():
    def __init__(self,_polygon,_color):
        self.color = _color
        self.polygon = _polygon
    def display(self,screen):
        pygame.gfxdraw.filled_polygon(screen, self.polygon.exterior.coords,self.color)
        pygame.gfxdraw.aapolygon(screen, self.polygon.exterior.coords,self.color)