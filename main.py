#Import della classe EspressioneRegolare dal modulo Kola_espreg
from Kola_espreg import EspressioneRegolare

def main():
    #Creazione di un'istanza della classe con un'espressione regolare per numeri interi
    regex_validatore = EspressioneRegolare(r'\d+')

    #Test di validazione con una stringa che corrisponde
    test_string1 = "123"
    result1 = regex_validatore.valida(test_string1)
    print(f"Test '{test_string1}': {result1}")



if __name__ == "__main__":
    main()
