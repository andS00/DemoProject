import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600

class Personaggio(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('imageG/bird.png')
        self.image = pygame.transform.scale(self.image, (100,100))

        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.velocita_x
        self.rect.y += self.velocita_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y


personaggio = Personaggio(100, 100)

gruppo_di_personaggi = pygame.sprite.Group()
gruppo_di_personaggi.add(personaggio)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gestione degli Sprite e movimento")

orologio = pygame.time.Clock()
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
    
    
  
    gruppo_di_personaggi.update()
   
    screen.fill("white")
    gruppo_di_personaggi.draw(screen)
    
    orologio.tick(frame_rate)
    
    
    
    pygame.display.update()