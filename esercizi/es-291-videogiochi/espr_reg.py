"""
Modulo per le espressioni regolari del progetto 291
"""
import re

# Validazione del codice prodotto: 1 lettera seguita da 3 numeri
PATTERN_CODICE_PRODOTTO = r'^[A-Z]\d{3}$'

def valida_codice_prodotto(codice):
    """
    Valida il formato del codice prodotto.
    Il codice deve essere composto da:
    - 1 carattere alfabetico maiuscolo (A-Z)
    - 3 caratteri numerici (0-9)
    
    Args:
        codice (str): Il codice da validare
    
    Returns:
        bool: True se il codice è valido, False altrimenti
    """
    return bool(re.match(PATTERN_CODICE_PRODOTTO, codice))
