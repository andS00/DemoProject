import socket
import pygame
import threading
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Impostazione rete
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Posizione iniziale del giocatore
player_pos = [100, 100]
# Dizionario per memorizzare le posizione degli altri giocatori
players = {}

# Funziona per ricevere i movimenti degli altri giocatori
def receive_data():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            # Data = (0, 100, 110)
            id, x, y = data.split(',')
            # Aggiorna la posizione del giocatore nel dizionario
            players[id] = (int(x), int(y))
        except:
            break

# Avvia un thread per ricevere i dati in background
threading.Thread(target=receive_data, daemon=True).start()

# Ciclo principale del gioco
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5
    
    # Invia la posizione del giocatore al server
    message = f"{player_pos[0]}, {player_pos[1]}"
    client_socket.sendall(message.encode())

    # Disegna tutto sullo schermo
    screen.fill("black")
    pygame.draw.rect(screen, (0, 255, 0), (*player_pos, 50, 50))

    # Disegna gli altri giocatori
    for pos in players.values():
        pygame.draw.rect(screen, (255, 0, 0), (*pos, 50, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()