##Crea in C# o Python una classe Veicolo e una classe Auto che eredita da Veicolo
##Effettua il commit delle modifiche
##Crea un nuovo branch per aggiungere un nuovo tipo di veicolo Moto
##Crea in C# o Python una classe Moto che eredita da Veicolo
##Effettua il commit delle modifiche
##Effettua il merge delle modifiche sul ramo principale
##Introduci per errore una modifica sbagliata (es. elimina un metodo o cambia il nome di una variabile) e fai dunque un commit errato
##Usa uno dei comandi visti a lezione per annullare o eliminare il commit errato
##Crea un repository remoto su GitHub (avrai bisogno di un account!)
##Simula una collaborazione con un tuo compagno
##Utilizzate i comandi per effettuare l’upload, il download e la verifica di sincronizzazione


class Veicolo :
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte