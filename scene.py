import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Gestione delle immagini")

# Caricamento dell'immagine
bkg = pygame.image.load("imageG/Space.jpg")
pers = pygame.image.load("imageG/bird.png")

# Ridimensionamento immagine
bkg = pygame.transform.scale(bkg, (800, 600))

pers = pygame.transform.scale(pers, (200, 200))

# Caricare il nostro font
font = pygame.font.Font(None, 36)

# Render del testo
testo = font.render('Benvenuti nel nostro gioco', True, ("red"))


pygame.display.flip()

# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # pygame.KEYDOWN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    
    screen.fill((255, 255, 255))

    # Posizionamento dell'immagine
    screen.blit(bkg, (0, 0))
    screen.blit(pers, (300, 350))

    screen.blit(testo, (100, 50))
    
    orologio.tick(frame_rate)
    
    
    
    pygame.display.update()