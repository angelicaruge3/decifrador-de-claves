import pytest 

from descifrador_de_claves import ordenamiento_por_mezcla

def test_ordenamiento_por_mezcla():

    lista_desordenada = [5, 2, 8, 1, 9, 0, 3, 7, 4, 6]

    lista_ordenada = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ordenamiento_por_mezcla(lista_desordenada) == lista_ordenada