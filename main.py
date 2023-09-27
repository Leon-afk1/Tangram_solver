from Shape import Shape
import pygame
import math
import shapely

pygame.init()

# test 1

# Important: 
# Les polygones sont scale up car sinon ils sont trop petits et ne s'affichent que sur 2 pixels
# c'est préferable de stoquer les points des polygones en échelle réduite pour permetre de les manipuler plus facilement
# le scaling se fait au moment de get les points
SCALE_FACTOR = 100

# setup pour la fenetre (osef tier)
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tangram')
screen.fill(background_colour)
running = True

# creation des objets, on peut ajouter autant de points qu'on veut
triPoints = [[0,0],[2,0],[2,2]]
rectPoints = [[0,0],[2,0],[2,2],[0,2]]
triangle = Shape(triPoints,[300,100],SCALE_FACTOR)
rectangle = Shape(rectPoints,[100,0],SCALE_FACTOR)


# test de rotation des polygones (angle en radiant)
rectangle.rotate(0.1223345234)
triangle.rotate(1.23465)

# affichage des polygones avec pygame
pygame.draw.polygon(screen, (255,0,0), triangle.getVertices())
pygame.draw.polygon(screen, (0,255,0), rectangle.getVertices())
pygame.draw.polygon(screen, (0,0,255), ((100, 140), (120, 120), (130, 160), (120, 160), (110, 180)))


# boucle servant a l'affichage 
# running est vrai tant que on ne ferme pas la fenetre
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    


