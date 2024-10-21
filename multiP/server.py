import socket
import threading

# Creazione di un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind indirizzo IP e porta
server_socket.bind(('localhost', 8080))
# Accetta massimo 2 connessioni simultaneamente
server_socket.listen(2)

clients = {}

def handle_client(client_socket, client_id):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Ricevuto dal client {client_id}: {data}")

            # Invia i dati a tutti gli altri client
            broadcast(data, client_id)

        except:
            break
    # Rimuovi il client disconnesso
    client_socket.close()
    del clients[client_id]
    print(f"Client {client_id} disconnesso")


# Funzione per mandare i dati a tutti gli altri client
def broadcast(message, sender_id):
    for client_id, client_socket in clients.items():
        if client_id != sender_id:
            try:
                client_socket.sendall(f"{sender_id}, {message}".encode())
            except:
                # Gestire le eccezioni in caso di problemi nell'invio
                pass

# Ciclo principale del server
def start_server():
    print(f"Server avviato. In attesa di connessioni...")
    client_id = 0;
    while True:
        client_socket, addr = server_socket.accept()
        clients[client_id] = client_socket
        print(f"Connesso a {addr} con ID {client_id}")

        # Avvia un thread per gestire il nuovo client
        threading.Thread(target=handle_client, args=(client_socket, client_id)).start()
        client_id += 1


if __name__ == "__main__":
    start_server()