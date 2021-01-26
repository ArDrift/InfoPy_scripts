#!/usr/bin/env python3

import random

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def helyben_keveres(lista):
  print("Keverés előtt:", lista)
  for i in range(0, len(lista) - 1):
    j = random.randint(i, len(lista) - 1)
    temp = lista[j]
    lista[j] = lista[i]
    lista[i] = temp
    print(lista)
    
  print("Keverés végén: ", lista)
  
  
def hatulrol_keveres(lista):
  print("Keverés előtt:", lista)
  for i in range(len(lista) - 1, 0, -1):
    j = random.randint(i, len(lista) - 1)
    temp = lista[j]
    lista[j] = lista[i]
    lista[i] = temp
    print(lista)
    
  print("Keverés végén: ", lista)


def ket_listas_keveres(lista):
  print("Keverés előtt:", lista)
  ujlista = []
  for i in range(0, len(lista)):
    j = random.randint(0, len(lista) - 1)
    ujlista.append(lista[j])
    lista.pop(j)
    print(lista)
    print(ujlista)
  
  print("Keverés végén: ", ujlista)


print("Helyben keverés: 0")
print("Keverés végéről eleje felé: 1")
print("Keverés két listával: 2")
valasztas = int(input("Add meg a keverés módját: "))

if valasztas == 0:
  helyben_keveres(lista)
elif valasztas == 1:
  hatulrol_keveres(lista)
elif valasztas == 2:
  ket_listas_keveres(lista)
