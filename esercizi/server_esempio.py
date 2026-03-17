"""Server TCP - per testare i client"""
import socket

porta_server = 6789

print(f"SERVER in attesa sulla porta {porta_server}...")

# Crea socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', porta_server))
server.listen(1)

# Accetta connessione
client, indirizzo = server.accept()
print(f"Client connesso da: {indirizzo[0]}:{indirizzo[1]}")

# Riceve dati
dati = client.recv(1024).decode('utf-8').strip()
print(f'Ricevuto dal client: "{dati}"')

# Risponde in maiuscolo
risposta = (dati.upper() + '\n').encode('utf-8')
client.sendall(risposta)
print(f'Inviato al client: "{dati.upper()}"')

# Chiude
client.close()
server.close()
print("Connessione chiusa.")