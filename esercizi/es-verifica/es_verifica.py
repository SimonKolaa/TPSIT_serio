import socket

# Crea un socket TCP/IP per il server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permette il riutilizzo della porta anche se è in stato TIME_WAIT
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Variabile per il socket del client (sarà assegnato dopo l'accept())
client_socket = None

# Lega il server alla porta 6789 (accetta connessioni su tutte le interfacce)
server_socket.bind(('', 6789))

# Mette il server in ascolto di connessioni in arrivo (1 = numero di connessioni in coda)
server_socket.listen(1)
print("Server in ascolto sulla porta 6789...")

# Accetta la connessione del client e ottiene l'indirizzo del client
client_socket, addr = server_socket.accept()
print(f"Connessione accettata da {addr}")

# Riceve i dati dal client (fino a 1024 byte)
stringa_ricevuta = client_socket.recv(1024)
print(f"Ricevuto: {stringa_ricevuta.decode()}")

# Prepara la risposta da inviare al client
stringa_modificata = 'CIAO'

# Invia la risposta al client (convertendo la stringa in bytes)
client_socket.send(stringa_modificata.encode())

# Chiude la connessione con il client
client_socket.close()

# Chiude il socket del server
server_socket.close()
print("Server chiuso.")