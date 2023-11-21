from functions import *
import pygame
from Piece import Piece
from EventManager import EventManager
from DisplayManager import DisplayManager
from ShapeGestion import ShapeGestion


(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tangram')


shape = Polygon([(0,565.685424949238), (565.685424949238,565.685424949238), (565.685424949238,0), (400,0), (0,400), (0,565.685424949238)])
bigTriangle1 = Piece(Polygon([(0,0),(400,0),(0,400)]),(0,255,154))
bigTriangle2 = Piece(Polygon([(0,0),(400,0),(0,400)]),(255,154,0))

p1 = Piece(shape,(255,0,0))

pieces = [p1,bigTriangle1,bigTriangle2]

ShapeGestion.saveFile("res/data.json",p1.poly)
ShapeGestion.importFile("res/data.json")
eventManager = EventManager(pieces)
displayManager = DisplayManager(pieces)

while eventManager.running:
    eventManager.Event()
    displayManager.Update(screen)
    