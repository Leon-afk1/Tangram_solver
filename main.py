import pygame
from pygame import gfxdraw
from math import sqrt
from shapely import *
from tangramSolver import *

pygame.init()

# test 2

# pour la fenetre (osef tier)
background_colour = (255,255,255)
(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tangram')
screen.fill(background_colour)
running = True
bigTriangle1 = Polygon([(0,0),(400,0),(0,400)])
squareShape = Polygon([(0, 0), (0, 400*sqrt(2)), (400*sqrt(2), 400*sqrt(2)), (400*sqrt(2), 0)])
polygon1 = Polygon([(0.5, -0.866025), (1, 0), (0.5, 0.866025), (-0.5, 0.866025), (-1, 0), (-0.5, -0.866025)])
polygon1 = transform(polygon1,lambda x:x*100+(100,100))
polygon2 = Polygon([(1, -0.866025), (1.866025, 0), (1, 0.866025), (0.133975, 0)])
polygon2 = transform(polygon2,lambda x:x*100+(100,100))
difference = polygon2.difference(polygon1)
polygons = MultiPolygon([squareShape, polygon1, polygon2,difference])

i = 50


for poly in polygons.geoms:
    #   2 lignes pour ajouter de l'antialiasing, on fill le rectangle et on rajoute les lignes exteieures antialiasé avec la deuxieme ligne
    #   ça existe pas avec pygame un polygone filled antialiased :(
    pygame.gfxdraw.filled_polygon(screen, poly.exterior.coords,(i,0,0))
    pygame.gfxdraw.aapolygon(screen, poly.exterior.coords,(i,0,0))
    
    i =i+50


solution = solveTangram(bigTriangle1,tangramPieces,screen)
print(solution)


#afficher les points du polygone avec pygame



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()