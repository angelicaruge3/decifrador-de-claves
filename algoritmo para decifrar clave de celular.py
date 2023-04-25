def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        mitad_izq = lista[:medio]
        mitad_der = lista[medio:]

        ordenamiento_por_mezcla(mitad_izq)
        ordenamiento_por_mezcla(mitad_der)

        a = 0
        b = 0
        c = 0

        while a < len(mitad_izq) and b < len(mitad_der):
            if mitad_izq[a] < mitad_der[b]:
                lista[c] = mitad_izq[a]
                a += 1
            else:
                lista[c] = mitad_der[b]
                b += 1
            c += 1

        while a < len(mitad_izq):
            lista[c] = mitad_izq[a]
            a += 1
            c += 1

        while b < len(mitad_der):
            lista[c] = mitad_der[b]
            b += 1
            c += 1

    return lista

def busqueda_binaria(lista, clave):
    abajo = 0
    alto = len(lista) - 1

    while abajo <= alto:
        medio = (abajo + alto) // 2

        if lista[medio] == clave:
            return medio
        elif lista[medio] < clave:
            abajo = medio + 1
        else:
            alto = medio - 1

    return -1

def adivinar_clave(clave, lista_organizada):
    lista_organizada = ordenamiento_por_mezcla(lista_organizada)
    clave_adivinada = ""

    for digit in clave:
        index = busqueda_binaria(lista_organizada, int(digit))

        if index != -1:
            clave_adivinada += str(index)
        else:
            clave_adivinada += digit

    return clave_adivinada


lista_desordenada = [5, 2, 8, 1, 9, 0, 3, 7, 4, 6]
lista_organizada = sorted(lista_desordenada)
print(lista_organizada)
clave=[]
for x in range(1):
    valor=int(input("ingresa el primer digito:"))
    clave.append (valor)
    print(valor)
    valor=int(input("ingresa el segundo digito:"))
    clave.append (valor)
    print(valor)
    valor=int(input("ingresa el tercer digito:"))
    clave.append (valor)
    print(valor)
    valor=int(input("ingresa el cuarto digito:"))
    clave.append (valor)
    print(valor)
print(clave)

clave_adivinada = adivinar_clave(clave, lista_organizada)
print(clave_adivinada)