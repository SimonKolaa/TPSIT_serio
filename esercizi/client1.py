"""Client TCP base - pag. 178-184"""
import socket

nome_server = "localhost"
porta_server = 6789

print("CLIENT partito in esecuzione...")

# Crea socket e connette
mio_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mio_socket.connect((nome_server, porta_server))

# Invia stringa
stringa = input("Invia la stringa da trasmettere al server: ")
mio_socket.sendall((stringa + '\n').encode('utf-8'))

# Riceve risposta
risposta = mio_socket.recv(1024).decode('utf-8').strip()
print(f"...risposta dal server: {risposta}")

mio_socket.close()
print("\nTermino elaborazione e chiudo connessione")
