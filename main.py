#Import della classe Pattern dal modulo Kola_espreg
from Kola_espreg import Pattern

def main():
    #Creazione di un'istanza della classe con un'espressione regolare per numeri interi
    regex_valida = Pattern(r'\d+')

    #Test di validazione con match (inizia con il pattern)
    test_string1 = "123"
    result1 = regex_valida.match_valida(test_string1)
    print(f"Test match '{test_string1}': {result1}")

    test_string2 = "123abc"
    result2 = regex_valida.match_valida(test_string2)
    print(f"Test match '{test_string2}': {result2}")

    #Test di validazione con fullmatch (corrisponde esattamente)
    result3 = regex_valida.fullmatch_valida(test_string1)
    print(f"Test fullmatch '{test_string1}': {result3}")

    result4 = regex_valida.fullmatch_valida(test_string2)
    print(f"Test fullmatch '{test_string2}': {result4}")


    #Test con la nuova espressione regolare
    test_string3 = "Hello"
    result5 = regex_valida.match_valida(test_string3)
    print(f"Test match '{test_string3}' con nuova regex: {result5}")

    result6 = regex_valida.fullmatch_valida(test_string3)
    print(f"Test fullmatch '{test_string3}' con nuova regex: {result6}")

    test_string4 = "Hello123"
    result7 = regex_valida.match_valida(test_string4)
    print(f"Test match '{test_string4}' con nuova regex: {result7}")

    result8 = regex_valida.fullmatch_valida(test_string4)
    print(f"Test fullmatch '{test_string4}' con nuova regex: {result8}")


    # Validazione intero
    int_test1 = "123"
    result_int1 = regex_valida.valida_intero(int_test1)
    print(f"Intero '{int_test1}': {result_int1}")

    int_test2 = "-456"
    result_int2 = regex_valida.valida_intero(int_test2)
    print(f"Intero '{int_test2}': {result_int2}")

    int_test3 = "abc"
    result_int3 = regex_valida.valida_intero(int_test3)
    print(f"Intero '{int_test3}': {result_int3}")

    # Validazione float
    float_test1 = "24.1632"
    result_float1 = regex_valida.valida_float(float_test1)
    print(f"Float '{float_test1}': {result_float1}")

    float_test2 = "-1.23e10"
    result_float2 = regex_valida.valida_float(float_test2)
    print(f"Float '{float_test2}': {result_float2}")

    float_test3 = "miao"
    result_float3 = regex_valida.valida_float(float_test3)
    print(f"Float '{float_test3}': {result_float3}")

if __name__ == "__main__":
    main()
