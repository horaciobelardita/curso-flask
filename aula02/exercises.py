def multiplicacion_por_suma(x, y):
    res = 0
    for _ in range(y):
        res += x
    return res


def imprimir_al_reves(nombre: str, apellido: str):
    completo = f"{nombre} {apellido}"
    return completo[::-1]


def menor_lista():
    import random
    from functools import reduce

    lista = [random.randint(1, 100) for i in range(1, 6)]
    return reduce(lambda prev, item: prev if prev < item else item, lista)


def volumen_esfera(radio):
    import math

    return 4 / 3 * math.pi * radio ** 3


def es_mayor(edad):
    return edad >= 18


def es_par(numero):
    return numero % 2 == 0


def contar_vocales(palabra):
    from functools import reduce

    vocales = "a,e,i,o,u".split(",")
    return reduce(
        lambda prev, letra: prev + 1 if letra.lower() in vocales else prev, palabra, 0
    )


def sumar_numeros():
    from functools import reduce

    numeros = []
    print("ingresar numeros y 0 para finalizar")
    while True:
        try:
            numero = int(input("Numero: "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            continue
    suma = reduce(lambda acum, num: acum + num, numeros, 0)
    print(f"lista -> {numeros}")
    print(f"suma -> {suma}")
