#!/usr/bin/env python3

import random

def ladarendezes(lista):
  dblista = []
  for i in range(max(lista) + 1):
    dblista.append(0)
    for elem in lista:
      if elem == i:
        dblista[i] += 1

  rendezett = []
  for i in range(len(dblista)):
    if dblista[i] != 0:
      for db in range(dblista[i]): 
        rendezett.append(i)
  
  return rendezett


def rendezett_e(lista):
  for i in range(len(lista) - 1):
    if lista[i] > lista[i+1]:
      return False

  return True


def main():
  lista = []
  for _ in range(100000):
    lista.append(random.randint(0, 99))

  print(rendezett_e(ladarendezes(lista)))


main()
