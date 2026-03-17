"""Client TCP flessibile - Mettiti alla prova pag. 185"""
import socket

# Input parametri dall'utente
nome_server = input("Inserisci indirizzo server (es. localhost): ")
porta_server = int(input("Inserisci porta server (es. 6789): "))

print(f"\nCLIENT partito in esecuzione...")
print(f"Connessione a {nome_server}:{porta_server}")

# Crea socket e connette
mio_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mio_socket.connect((nome_server, porta_server))
print("Connesso!\n")

# Invia stringa
stringa = input("Invia la stringa da trasmettere al server: ")
mio_socket.sendall((stringa + '\n').encode('utf-8'))

# Riceve risposta
risposta = mio_socket.recv(1024).decode('utf-8').strip()
print(f"Risposta dal server: {risposta}")

mio_socket.close()
print("\nConnessione chiusa.")
