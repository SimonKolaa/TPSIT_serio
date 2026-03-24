import socket

PORTA = 6789
BUFFER = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", PORTA))

attivo = True
print("SERVER avviato...")

while attivo:
    # attesa ricezione dato dal client
    dati, indirizzo_client = server_socket.recvfrom(BUFFER)
    ricevuto = dati.decode()
    print("RICEVUTO:", ricevuto)

    # controllo termine esecuzione del server
    if ricevuto == "fine":
        print("SERVER IN CHIUSURA")
        attivo = False
    else:
        # risposta: messaggio in maiuscolo
        risposta = ricevuto.upper()
        server_socket.sendto(risposta.encode(), indirizzo_client)

server_socket.close()