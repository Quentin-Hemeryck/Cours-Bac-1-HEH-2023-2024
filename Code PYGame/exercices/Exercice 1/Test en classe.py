import pygame
pygame.init()

#notre joueur
class Player(pygame.sprite.Sprite):



#INIT
fenetre = (600,600)

surface = pygame.display.set_mode(fenetre, pygame.RESIZABLE)
maCouleur = (0, 255, 0) #couleur vert
surface.fill(maCouleur)


running = True
#GAME LOOP
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pygame.display.flip()

