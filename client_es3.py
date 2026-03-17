import socket

# Equivalente a: public class Multiclient
class MultiClient:
    def __init__(self, nome_server='localhost', porta_server=6789):
        self.nome_server = nome_server
        self.porta_server = porta_server
        self.miosocket = None
        self.out_verso_server = None
        self.in_dal_server = None

    def connetti(self):
        print("2 CLIENT partito in esecuzione ...")
        try:
            self.miosocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.miosocket.connect((self.nome_server, self.porta_server))
            # Stream di lettura/scrittura (equivalente a DataOutputStream e BufferedReader)
            self.out_verso_server = self.miosocket.makefile('w', encoding='utf-8')
            self.in_dal_server    = self.miosocket.makefile('r', encoding='utf-8')
        except ConnectionRefusedError:
            print("Host sconosciuto o server non raggiungibile")
            exit(1)
        except Exception as e:
            print(e)
            print("Errore durante la connessione!")
            exit(1)
        return self.miosocket

    def comunica(self):
        # Loop infinito: termina quando l'utente scrive FINE
        while True:
            print("4 ... utente, inserisci la stringa da trasmettere al server:")
            stringa_utente = input()

            # Spedisco al server
            print("5 ... invio la stringa al server e attendo ...")
            self.out_verso_server.write(stringa_utente + '\n')
            self.out_verso_server.flush()

            # Leggo la risposta dal server
            stringa_ricevuta = self.in_dal_server.readline().rstrip('\n')
            print(f"7 ... risposta dal server\n{stringa_ricevuta}")

            if stringa_utente == "FINE":
                print("8 CLIENT: termina elaborazione e chiude connessione")
                self.miosocket.close()
                break

    def run(self):
        self.connetti()
        self.comunica()


if __name__ == "__main__":
    client = MultiClient()
    client.run()