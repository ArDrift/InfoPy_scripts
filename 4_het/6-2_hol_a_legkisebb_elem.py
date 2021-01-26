#!/usr/bin/env python3

lista = [12, 43, 10, 32, 93, 1, 23, 40, 26, 11, 10]
legkisebb = lista[0]

print("A lista:", end="")
for elem in range(0, len(lista)):
  print("", "[{}]={}".format(elem, lista[elem]), end="")
  
  if lista[elem] < legkisebb:
    legkisebb = lista[elem]
  
print("")
print("A legkisebb szám:", legkisebb)
