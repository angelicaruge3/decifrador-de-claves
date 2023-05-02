import pytest
from algoritmo para decifrar clave de celular import ordenamiento_por_mezcla

def test_ordenamiento_por_mezcla():
    assert ordenamiento_por_mezcla(3,4,6,2,1,8,7,0,9)
    
def  test_ordenamiento_por_mezcla():
    assert ordenamiento_por_mezcla(5,3,4,6,2,1,8,7,0)
    

import pytest
from algoritmo para decifrar clave de celular import busqueda_binaria

def test_busqueda_binaria():
    assert busqueda_binaria(1,4,3,6,7,2,8,9,5)==2
    

def test_busqueda_binaria():
    assert busqueda_binaria(1,4,3,6,7,2,8,9,5)==5
    
def test_busqueda_binaria():
    assert busqueda_binaria(1,4,3,6,7,2,8,9,5)==9
    
def test_busqueda_binaria():
    assert busqueda_binaria(1,4,3,6,7,2,8,9,5)==1
    
    
import pytest
from algoritmo para decifrar clave de celular import adivinar_clave

def test_adivinar_clave():
    assert adivinar_clave(1,2,3,5,4,6,7,9,8)==1234
    
def test_adivinar_clave():
    assert adivinar_clave(1,2,3,5,4,6,7,9,8)==2345
    
def test_adivinar_clave():
    assert adivinar_clave(1,2,3,5,4,6,7,9,8)==5678
    
def test_adivinar_clave():
    assert adivinar_clave(1,2,3,5,4,6,7,9,8)==7231