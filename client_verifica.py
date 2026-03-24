import socket

# Crea un socket TCP/IP per il client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definisce i parametri del server a cui connettersi
server_name = "localhost"
server_port = 6789

# Stabilisce la connessione con il server
print(f"Connessione al server {server_name}:{server_port}...")
client_socket.connect((server_name, server_port))
print("Connessione riuscita!")

# Prepara il messaggio da inviare al server
messaggio = "ciao"

# Invia il messaggio al server (convertendo la stringa in bytes)
client_socket.send(messaggio.encode())
print(f"Messaggio inviato: {messaggio}")

# Riceve la risposta dal server (fino a 1024 byte)
risposta = client_socket.recv(1024)
print(f"Risposta ricevuta: {risposta.decode()}")

# Chiude la connessione con il server
client_socket.close()
print("Connessione chiusa.")