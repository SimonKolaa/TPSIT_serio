import socket

PORTA_SERVER = 6789
IP_SERVER = "localhost"
BUFFER = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client pronto - inserisci un dato da inviare:")
da_spedire = input()

# invio al server
client_socket.sendto(da_spedire.encode(), (IP_SERVER, PORTA_SERVER))

# se non è "fine", aspetta la risposta
if da_spedire != "fine":
    dati, _ = client_socket.recvfrom(BUFFER)
    ricevuto = dati.decode()
    print("dal SERVER:", ricevuto)

client_socket.close()