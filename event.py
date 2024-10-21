import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Eventi personalizzati")

# Colori
bianco = (255, 255, 255)
nero = (0, 0, 0)
blu = (0, 0, 255)
rosso = (255, 0, 0)
arancione = (255, 117, 20)

# Evento personalizzato
event_counter = 1
TOCCO_BORDO = pygame.USEREVENT + event_counter
event_counter+=1

colore_personaggio = arancione
class Personaggio(pygame.sprite.Sprite):
    # Costruttore della classe
    def __init__(self, x, y):
        # Chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        # Carichiamo immagine per personaggio
        self.image = pygame.image.load("imageG/bird.png")
        # Ridimensioniamo il personaggio
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Rettangolo di posizione e collisione
        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

    def update(self):
        self.rect.x += self.velocita_x
        self.rect.y += self.velocita_y
        # Controllo dei limiti dello schermo
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
        if self.rect.left <= 0 or self.rect.right >= WIDTH or self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            pygame.event.post(pygame.event.Event(TOCCO_BORDO))

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

    def cambia_colore(self, colore):
        self.image.fill(colore)

# Creazione del rettangolo
personaggio = Personaggio(100,100)
all_sprites = pygame.sprite.Group()
all_sprites.add(personaggio)
# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                personaggio.cambia_velocita(-5, 0)
            if event.key == pygame.K_RIGHT:
                personaggio.cambia_velocita(5, 0)
            if event.key == pygame.K_UP:
                personaggio.cambia_velocita(0, -5)
            if event.key == pygame.K_DOWN:
                personaggio.cambia_velocita(0, 5)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                personaggio.cambia_velocita(5, 0)
            if event.key == pygame.K_RIGHT:
                personaggio.cambia_velocita(-5, 0)
            if event.key == pygame.K_UP:
                personaggio.cambia_velocita(0, 5)
            if event.key == pygame.K_DOWN:
                personaggio.cambia_velocita(0, -5)
        elif event.type == TOCCO_BORDO:
            if colore_personaggio == arancione:
                colore_personaggio = blu
            else:
                colore_personaggio = arancione
            personaggio.cambia_colore(colore_personaggio)
    
    screen.fill(bianco)
    all_sprites.update()
    all_sprites.draw(screen)
    orologio.tick(frame_rate)
    
    pygame.display.update()