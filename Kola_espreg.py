#una classe (ad es. EsprReg) che data una espressione regolare e una stringa valida quest'ultima, ovvero restituisce a video il testo "match" oppure "mismatch".
#In particolare si vogliono vedere:
#1. attributi e metodi con gli opportuni modificatori di classe
#2. almeno due metodi di cui uno che riceve in input l'espressione regolare e l'altro che effettua il test per la validazione e restituisce l'output suddetto
#3a. il costruttore della vostra classe (potete anche estenderne una già prevista se preferite) e un'istanza della vostra classe nel main in cui vengono richiamati i metodi di cui sopra 
#3b. in alternativa potete anche creare una classe di utilità con metodi e proprietà statici e utilizzarla opportunamente nel main in cui vengono richiamati i metodi di cui sopra
#4. codice ben indentato, commentato e modulare (ovvero un file dedicato per ogni parte logica del programma). 

import re
class EspressioneRegolare:
    def __init__(self, tipo: str):
        #Costruttore che inizializza l'espressione regolare
        self.tipo = tipo

    def set_tipo(self, tipo: str):
        #Metodo per impostare una nuova espressione regolare
        self.tipo = tipo

    def valida(self, string: str) -> str: ##type hinting
        #Metodo che verifica se la stringa corrisponde all'espressione regolare
        if re.fullmatch(self.tipo, string):
            return "match"
        else:
            return "mismatch"