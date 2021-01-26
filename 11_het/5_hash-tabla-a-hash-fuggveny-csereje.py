#!/usr/bin/env python3

def hash_tabla_letrehoz(meret):
  tabla = []
  for i in range(meret):
    tabla.append([])
    
  return tabla


def hash_tabla_betesz(tabla, szo):
  kulcs = hash(szo)
  meret = len(tabla)
  if szo not in tabla[kulcs % meret]:
    tabla[kulcs % meret].append(szo)

  return tabla


def hash_tabla_debug(tabla):
  for i in range(len(tabla)):
    print("{:2}: {}".format(i, tabla[i]))


def hash_tabla_benne_van(tabla, szo):
  kulcs = hash(szo)
  meret = len(tabla)
  return szo in tabla[kulcs % meret]


def hash_tabla_kivesz(tabla, szo):
  kulcs = hash(szo)
  meret = len(tabla)
  if szo in tabla[kulcs % meret]:
    tabla[kulcs % meret].remove(szo)

  return tabla


def hash_tabla_listaz(tabla):
   for lista in tabla:
     for elem in lista:
       print(elem, end=" ")
       
   print("")


def main():
  hasht = hash_tabla_letrehoz(20)

  hash_tabla_betesz(hasht, "eper")
  assert(hash_tabla_benne_van(hasht, "eper") == True)
  hash_tabla_betesz(hasht, "alma")
  assert(hash_tabla_benne_van(hasht, "alma") == True)
  hash_tabla_betesz(hasht, "zab")
  assert(hash_tabla_benne_van(hasht, "zab") == True)
  hash_tabla_betesz(hasht, "ananasz")
  assert(hash_tabla_benne_van(hasht, "ananasz") == True)
  
  hash_tabla_kivesz(hasht, "zab")
  assert(hash_tabla_benne_van(hasht, "zab") == False)
  
  #hash_tabla_debug(hasht)
  assert(hash_tabla_benne_van(hasht, "alma") == True)
  hash_tabla_listaz(hasht)


main()
