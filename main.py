import pygame

pygame.init()

#crée fenetre du jeux
x= 800
y= 600
pygame.display.set_mode((x,y))
pygame.display.set_caption("Pygame")


#boucle du jeux

running = True

while running :
    for evenet in pygame.event.get():
        if evenet.type == pygame.QUIT:
            running = False

pygame.quit()