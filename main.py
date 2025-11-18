#Import della classe EspressioneRegolare dal modulo Kola_espreg
from Kola_espreg import EspressioneRegolare

def main():
    #Creazione di un'istanza della classe con un'espressione regolare per numeri interi
    regex_validatore = EspressioneRegolare(r'\d+')

    #Test di validazione con una stringa che corrisponde
    test_string1 = "123"
    risultato1 = regex_validatore.valida(test_string1)
    print(f"Test '{test_string1}': {risultato1}")

#Test di validazione con una stringa che non corrisponde
    test_string2 = "abc"
    risultato2 = regex_validatore.valida(test_string2)
    print(f"Test '{test_string2}': {risultato2}")


#Cambiamento dell'espressione regolare utilizzando il metodo set_tipo
    regex_validatore.set_tipo(r'[a-zA-Z]+')


#Test con la nuova espressione regolare
    test_string3 = "Hello"
    risultato3 = regex_validatore.valida(test_string3)
    print(f"Test '{test_string3}' con nuova regex: {risultato3}")


    test_string4 = "123"
    risultato4 = regex_validatore.valida(test_string4)
    print(f"Test '{test_string4}' con nuova regex: {risultato4}")



if __name__ == "__main__":
    main()
