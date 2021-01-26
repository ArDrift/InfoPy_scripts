#!/usr/bin/env python3

def rendezes(lista):
  legn = lista.index(max(lista))
  maxrange = list(lista[:legn + 1])
  maxrange.reverse()
  rendezett = maxrange + list(lista[legn + 1:])
  print("1. fordítás után: {}".format(rendezett))
  rendezett.reverse()
  
  print("2. fordítás után: {}".format(rendezett))
  return rendezett


def main():
  l = [3, 1, 2, 4, 6, 7, 10, 9, 8, 5]
  rendezett = list(l)
  for i in range(len(l)):
    rendezett = rendezes(rendezett[0: -i])


main()
