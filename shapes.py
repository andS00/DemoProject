import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,600))
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
    
    
    screen.fill("white")
    pygame.draw.circle(screen, "pink", (400, 300), 200)
    pygame.draw.circle(screen, "blue", (500, 250), 20)
    pygame.draw.circle(screen, "blue", (300, 250), 20)
    pygame.draw.line(screen, ("black"), (300,400), (500,400), 5)

    #pygame.draw.rect(screen,(127,0,255),(100,50,100,50), 2)
    #pygame.draw.line(screen, (0, 0, 0), (100,400), (700,400), 5)
    #pygame.draw.polygon(screen, (0,0,0), [(300, 200),(400,100),(500,200),(500,300),(300,300) ], 5)
    orologio.tick(frame_rate)

    pygame.display.update()    