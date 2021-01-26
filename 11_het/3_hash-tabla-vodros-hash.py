#!/usr/bin/env python3

def hash_tabla_letrehoz():
  tabla = []
  for i in range(26):
    tabla.append([])
    
  return tabla


def key(szo):
  if ord(szo[0]) >= 97 and ord(szo[0]) <= 122:
    return ord(szo[0])
  else:
    raise ValueError("A(z) '{}' karakter nem hashelhető, adj meg ékezet nélküli, kisbetűvel kezdődő szót.".format(szo[0]))


def hash_tabla_betesz(tabla, szo):
  kulcs = key(szo)
  if szo not in tabla[kulcs - 97]:
    tabla[kulcs - 97].append(szo)

  return tabla


def hash_tabla_debug(tabla):
  for i in range(len(tabla)):
    print("{:2} ({}): {}".format(i, chr(i + 97), tabla[i]))


def hash_tabla_benne_van(tabla, szo):
  kulcs = key(szo)
  return szo in tabla[kulcs - 97]


def hash_tabla_kivesz(tabla, szo):
  kulcs = key(szo)
  if szo in tabla[kulcs - 97]:
    tabla[kulcs - 97].remove(szo)

  return tabla


def hash_tabla_listaz(tabla):
   for lista in tabla:
     for elem in lista:
       print(elem, end=" ")
       
   print("")


def main():
  hasht = hash_tabla_letrehoz()

  hash_tabla_betesz(hasht, "eper")
  hash_tabla_betesz(hasht, "alma")
  hash_tabla_betesz(hasht, "zab")
  hash_tabla_betesz(hasht, "ananasz")
  
  hash_tabla_kivesz(hasht, "ananasz")
  
  #hash_tabla_debug(hasht)
  #print(hash_tabla_benne_van(hasht, "ananasz"))
  hash_tabla_listaz(hasht)


main()
