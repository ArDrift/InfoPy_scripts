#!/usr/bin/env python3

def bin_ker(q, lista, eleje, vege):
    kozep = (eleje + vege) // 2
    if eleje <= vege:
        if q == lista[kozep]:
            return kozep
        elif q > lista[kozep]:
            return bin_ker(q, lista, kozep + 1, vege)
        elif q < lista[kozep]:
            return bin_ker(q, lista, eleje, kozep-1)
    else:
        return kozep+1


def halmaz_letrehoz(*args):
    lista = []
    for elem in args:
        idx = bin_ker(elem, lista, 0, len(lista)-1)
        lista.insert(idx, elem)
    return lista


def halmaz_betesz(elem, lista):
    idx = bin_ker(elem, lista, 0, len(lista)-1)
    lista.insert(idx, elem)


def halmaz_eleme_e(elem, lista):
    idx = bin_ker(elem, lista, 0, len(lista)-1)
    if idx <= len(lista)-1:
        if lista[idx] == elem:
            return True
        else:
            return False
    return False


def halmaz_kivesz(elem, lista):
    if halmaz_eleme_e(elem, lista):
        idx = bin_ker(elem, lista, 0, len(lista)-1)
        lista.pop(idx)        


def halmaz_unio(lista1, lista2):
    idx1 = 0
    idx2 = 0
    res = []
    while idx1 <= len(lista1)-1 or idx2 <= len(lista2)-1:
        if idx1 <= len(lista1)-1 and (idx2 >= len(lista2) or lista1[idx1] <= lista2[idx2]):
            res.append(lista1[idx1])
            if idx2 <= len(lista2)-1 and lista2[idx2] == lista1[idx1]:
                idx2 += 1
            idx1 += 1
        else:
            res.append(lista2[idx2])
            if idx1 <= len(lista1)-1 and lista1[idx1] == lista2[idx2]:
                idx1 += 1
            idx2 += 1
    return res


def halmaz_metszet(lista1, lista2):
    idx1 = 0
    idx2 = 0
    res = []
    while idx1 <= len(lista1)-1 and idx2 <= len(lista2)-1:
        if lista1[idx1] == lista2[idx2]:
            res.append(lista1[idx1])
            idx2 += 1
            idx1 += 1
        elif idx1 <= len(lista1)-1 and (idx2 >= len(lista2) or lista1[idx1] <= lista2[idx2]):
            idx1 += 1
        else:
            idx2 += 1
    return res


def halmaz_egyenlo_e(lista1, lista2):
    return halmaz_metszet(lista1, lista2) == halmaz_unio(lista1, lista2)


def main():
    tomb = [1, 10, 12, 22, 391, 3932]
    assert(bin_ker(11, tomb, 0, len(tomb)-1) == 2)
    assert(bin_ker(2333929191, tomb, 0, len(tomb)-1) == 6)
    halmaz_betesz(3939, tomb)
    assert(bin_ker(3939, tomb, 0, len(tomb)-1) == 6)
    halmaz_betesz(0, tomb)
    assert(bin_ker(0, tomb, 0, len(tomb)-1) == 0)
    
    assert(halmaz_eleme_e(10, tomb) == True)
    assert(halmaz_eleme_e(3932992, tomb) == False)
    
    teszt = halmaz_letrehoz(11, 10, 1, 332, 9, 32)
    assert(teszt == [1, 9, 10, 11, 32, 332])

    assert(halmaz_unio(tomb, teszt) == [0,1,9,10,11,12,22,32,332,391,3932,3939])
    assert(halmaz_metszet(tomb, teszt) == [1, 10])
    
    assert(halmaz_egyenlo_e(halmaz_letrehoz(1, 4, 10, 9), halmaz_letrehoz(4, 10, 9, 1)) == True)
    assert(halmaz_egyenlo_e(halmaz_letrehoz(100, 2, 0), halmaz_letrehoz(100, 1, 0)) == False)


main()
