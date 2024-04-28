# Importe et initialise la bibliothèque Pygame
import pygame
pygame.init()

# Configure la surface de dessin
surface = pygame.display.set_mode((800, 600))

# Donne un nom à la fenêtre du programme
pygame.display.set_caption('RESUME PYGAME')

#couleur RGB
rouge = (255, 0, 0) #0 signifie aucune couleur, 255 signifie la couleur maximale
vert = (0, 255, 0) #0 signifie aucune couleur, 255 signifie la couleur maximale
bleu = (0, 0, 255) #0 signifie aucune couleur, 255 signifie la couleur maximale
noir = (0, 0, 0) #0 signifie aucune couleur, 255 signifie la couleur maximale
color = (rouge)

surface.fill(color) # Remplit la surface avec la couleur spécifiée

# Dessine un ligne noire
pygame.draw.line(surface, noir, (50, 50), (200, 200))

# Dessine un rectangle noir
pygame.draw.rect(surface, noir, (50, 50, 200, 100))

# Dessine un rectangle noir sans remplissage
pygame.draw.rect(surface, noir, (50, 200, 200, 100), 5)

# Dessine un rectangle noir sans remplissage avec coins arrondis
pygame.draw.rect(surface, noir, (50, 350, 200, 100), 5, 10)

# Dessine un cercle noir
pygame.draw.circle(surface, noir, (400, 150), 50)

# Dessine un cercle noir sans remplissage
pygame.draw.circle(surface, noir, (400, 300), 50, 5)

# Dessine un polygone noir
pygame.draw.polygon(surface, noir, [(400, 400), (500, 500), (600, 400)])

# Dessine un polygone noir sans remplissage
pygame.draw.polygon(surface, noir, [(400, 500), (500, 600), (600, 500)], 5)




pygame.display.flip() # Met à jour l'affichage


# Game Loop - Le programme s'exécute jusqu'à ce
# que l'utilisateur quitte l'application
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get(): # Parcours de tous les événements reçus
        if event.type == pygame.QUIT: # Si l'événement est de type QUIT (fermeture de la fenêtre)
            running = False




