from datetime import time
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()



# INITIALISATION DU JEU
pygame.init()
taille = (1000, 600)
surface = pygame.display.set_mode(taille)

pygame.display.set_caption("Projet d'étude !  - Concept")
# SURFACE DE JEU
r = 165
g = 105
b = 189
color = (r, g, b)
surface.fill(color)
pygame.display.flip()

# Dessiner une ligne
a = (30, 40)
b = (500, 250)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
pygame.draw.line(surface, rouge, a, b)
pygame.display.flip()

# Rectangle
rectangleRouge = pygame.Rect(350, 0, 20, 200)
rectangleBleu = pygame.Rect(0, 0, 60, 20)

# Charger une image
image_originale = pygame.image.load("img/img_1.png")
# Redimensionner l'image à la taille désirée
image_redimensionnee = pygame.transform.scale(image_originale,
                                              (image_originale.get_width() // 2, image_originale.get_height() // 2))

# Rendu du texte
font = pygame.font.Font("fonts/comic.ttf", 40)
texte = font.render("Messi Goat!", True, bleu)

# BOUCLE DE JEU (GAME LOOP)
en_cours = True
collision = False
deplacement_droite = True
while en_cours:
    # Gestion des événements
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            en_cours = False

    # Récupérer les touches appuyées en début de trame
    touches = pygame.key.get_pressed()
    # Déplacer le joueur en fonction des touches appuyées
    if touches[pygame.K_z]:
        rectangleBleu.move_ip(0, -1)
    if touches[pygame.K_q]:
        rectangleBleu.move_ip(-1, 0)
    if touches[pygame.K_s]:
        rectangleBleu.move_ip(0, 1)
    if touches[pygame.K_d]:
        rectangleBleu.move_ip(1, 0)

    # Vérifier la collision
    if rectangleBleu.colliderect(rectangleRouge):
        collision = True
    else:
        collision = False

    # Déplacer le rectangle bleu
    if deplacement_droite:
        rectangleBleu.move_ip(1, 0)
        if collision:
            deplacement_droite = False
    else:
        rectangleBleu.move_ip(-1, 0)
        if rectangleBleu.left <= 0:
            deplacement_droite = True

    # Redessiner tout
    surface.fill(color)
    pygame.draw.rect(surface, bleu, rectangleBleu)
    pygame.draw.rect(surface, rouge, rectangleRouge)
    surface.blit(image_redimensionnee, (2, 200))  # Afficher l'image redimensionnée
    surface.blit(texte, (2, 3))
    pygame.display.flip()







