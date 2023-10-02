import pygame
from pygame import gfxdraw
import math
from shapely import *
from functions import *

pygame.init()

# test 1

# pour la fenetre (osef tier)
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tangram')
screen.fill(background_colour)
running = True
 
poly_1 = Polygon([(180, 200), (280, 160), (250, 70), (160, 190)])
poly_2 = Polygon([(20, 200), (60, 260), (190, 210), (160, 130)])
poly_3 = poly_1.intersection(poly_2)
print(poly_1.intersection(poly_2))
polygons = MultiPolygon([poly_1, poly_2, poly_3])

i = 50


for poly in polygons.geoms:
    #   2 lignes pour ajouter de l'antialiasing, on fill le rectangle et on rajoute les lignes exteieures antialiasé avec la deuxieme ligne
    #   ça existe pas avec pygame un polygone filled antialiased :(

    pygame.gfxdraw.filled_polygon(screen, poly.exterior.coords,(i,0,0))
    pygame.gfxdraw.aapolygon(screen, poly.exterior.coords,(i,0,0))
    i =i+100

#afficher les points du polygone avec pygame

print(fullyIn(poly_3,poly_1))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()