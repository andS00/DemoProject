import pygame
import sys
pygame.init()


screen = pygame.display.set_mode((800,600))
screen.fill("white")


font = pygame.font.Font(None, 24)
testo = font.render("Benvenuti", True, "yellow")
    
    
pygame.quit()