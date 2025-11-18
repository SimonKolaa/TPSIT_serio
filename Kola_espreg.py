#una classe (ad es. EsprReg) che data una espressione regolare e una stringa valida quest'ultima, ovvero restituisce a video il testo "match" oppure "mismatch".
#In particolare si vogliono vedere:
#1. attributi e metodi con gli opportuni modificatori di classe
#2. almeno due metodi di cui uno che riceve in input l'espressione regolare e l'altro che effettua il test per la validazione e restituisce l'output suddetto
#3a. il costruttore della vostra classe (potete anche estenderne una già prevista se preferite) e un'istanza della vostra classe nel main in cui vengono richiamati i metodi di cui sopra 
#3b. in alternativa potete anche creare una classe di utilità con metodi e proprietà statici e utilizzarla opportunamente nel main in cui vengono richiamati i metodi di cui sopra
#4. codice ben indentato, commentato e modulare (ovvero un file dedicato per ogni parte logica del programma). 

import re

class Pattern:
    def __init__(self, regex: str):
        #Costruttore che inizializza il pattern compilato
        self.pattern = re.compile(regex)

    def set_regex(self, regex: str):
        #Metodo per impostare una nuova espressione regolare e ricompilarla
        self.pattern = re.compile(regex)

    def match_valida(self, string: str) -> str:
        #Metodo che verifica se la stringa inizia con il pattern (usando match)
        if self.pattern.match(string):
            return "match"
        else:
            return "mismatch"

    def fullmatch_valida(self, string: str) -> str: #type hinting
        #Metodo che verifica se la stringa corrisponde esattamente al pattern (usando fullmatch)
        if self.pattern.fullmatch(string):
            return "match"
        else:
            return "mismatch"

    def valida_intero(self, string: str) -> str: #type hinting
        # Valida un intero con segno opzionale
        int_pattern = re.compile(r'[-+]?\d+') #preso da libreria
        if int_pattern.fullmatch(string):
            return "match"
        else:
            return "mismatch"

    def valida_float(self, string: str) -> str: #type hinting
        # Valida un numero float
        float_pattern = re.compile(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?') ##preso da libreria
        if float_pattern.fullmatch(string):
            return "match"
        else:
            return "mismatch"