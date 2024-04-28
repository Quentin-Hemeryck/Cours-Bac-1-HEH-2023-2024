import pygame
import random

pygame.init()

# Fenetre
fenetre = (600, 600)
surface = pygame.display.set_mode(fenetre, pygame.RESIZABLE)
maCouleur = (0, 255, 0)  # couleur vert
surface.fill(maCouleur)

# Chargement de l'image de fond du jeu
fond = pygame.image.load("img/mountain.png").convert_alpha()
foret = pygame.image.load("img/foret.png").convert_alpha()
foret_rect = foret.get_rect(topleft=(0, 0))

#icon
pygame.display.set_icon(pygame.image.load("img/fireball.png"))


# Position initiale de la forêt
foret_x = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Chargement des 6 x images
        self.anim01 = pygame.image.load("img/bird_01.png").convert_alpha()
        self.anim02 = pygame.image.load("img/bird_02.png").convert_alpha()
        self.anim03 = pygame.image.load("img/bird_03.png").convert_alpha()
        self.anim04 = pygame.image.load("img/bird_04.png").convert_alpha()
        self.anim05 = pygame.image.load("img/bird_05.png").convert_alpha()
        self.anim06 = pygame.image.load("img/bird_06.png").convert_alpha()

        # Séquence
        self.animation = [self.anim01, self.anim02, self.anim03, self.anim04, self.anim05, self.anim06]

        # Index liste
        self.indexAnim = 0

        # Dessiner la représentation en 2D => 1ère image
        self.surf = self.animation[self.indexAnim]
        self.rect = self.surf.get_rect(midbottom=(fenetre[0] // 2, fenetre[1] // 2))

        # Vitesse de déplacement
        self.speed = 5

    def playerAnimation(self):
        self.indexAnim += 1
        if self.indexAnim > 5:
            self.indexAnim = 0

        self.surf = self.animation[self.indexAnim]

    def update(self, pressed_keys):
        # détecter l'appui
        if pressed_keys[pygame.K_z]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[pygame.K_q]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)

        # limiter déplacement
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > fenetre[0]:
            self.rect.right = fenetre[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > fenetre[1]:
            self.rect.bottom = fenetre[1]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("img/fireball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = fenetre[0]  # Début à droite de la fenêtre
        self.rect.y = random.randint(0, fenetre[1] - self.rect.height)  # Position aléatoire en Y
        self.speed_x = random.randint(3, 6)  # Vitesse aléatoire

    def update(self):
        self.rect.x -= self.speed_x
        if self.rect.right < 0:  # Si la boule sort de l'écran, la replacer à droite avec une nouvelle vitesse
            self.rect.x = fenetre[0]
            self.rect.y = random.randint(0, fenetre[1] - self.rect.height)
            self.speed_x = random.randint(3, 6)


# INIT

# Gestion des FPS
clock = pygame.time.Clock()

# Evenement personnel, apparait toutes les 150ms
eventAnimation = pygame.USEREVENT + 1
pygame.time.set_timer(eventAnimation, 50)

# Mon objet oiseau
oiseau = Player()

# Créer un groupe pour les ennemis
enemy_group = pygame.sprite.Group()

# Nombre maximum de boules de feu à l'écran
MAX_ENEMIES = 5

running = True
# GAME LOOP
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == eventAnimation:
            oiseau.playerAnimation()

            # Ajouter un nouvel ennemi à intervalles réguliers si le nombre d'ennemis est inférieur au maximum
            if len(enemy_group) < MAX_ENEMIES:
                new_enemy = Enemy()
                enemy_group.add(new_enemy)

        # Redimensionnement de la fenêtre
        if e.type == pygame.VIDEORESIZE:
            fenetre = e.dict['size']
            surface = pygame.display.set_mode(fenetre, pygame.RESIZABLE)
            surface.fill(maCouleur)

    # Gérer les touches pressées pour le déplacement du joueur
    oiseau.update(pygame.key.get_pressed())

    # Mettre à jour les ennemis
    enemy_group.update()

    # Dessiner le fond
    surface.fill((255, 255, 255))  # Remplir la surface avec une couleur blanche pour effacer le fond précédent
    # Redimensionner et dessiner le fond
    fond_redimensionne = pygame.transform.scale(fond, fenetre)
    surface.blit(fond_redimensionne, (0, 0))

    # Mettre à jour la position de la forêt
    foret_x -= 1
    if foret_x < -fenetre[0]:  # Si la forêt sort de l'écran, la replacer à droite de l'écran
        foret_x = 0

    # Dessiner la forêt
    surface.blit(foret, (foret_x, 0))
    surface.blit(foret, (foret_x + fenetre[0], 0))

    # Dessiner les ennemis
    enemy_group.draw(surface)

    # Dessiner le joueur
    surface.blit(oiseau.surf, oiseau.rect)

    # Dessiner
    pygame.display.flip()

    # Définir 60 FPS
    clock.tick(60)
