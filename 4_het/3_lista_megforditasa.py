#!/usr/bin/env python3

eredeti = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
forditott = []

def visszafele_forditott(lista):
  for elem in range(len(lista) - 1, -1, -1):
    forditott.append(lista[elem])
  print(forditott)


def vegerol_forditott(lista):
  for elem in range(len(lista) - 1, -1, -1):
    forditott.append(lista.pop())
  print(forditott)


def cserelo_forditott(lista):
  cserelendo = lista[0]
  for elem in range((len(lista)) // 2):
    cserelendo = lista[elem]
    lista[elem] = lista[len(lista) - 1 - elem]
    lista[len(lista) - 1 - elem] = cserelendo
  print(lista)

print("Lista fordítása visszafelé: 0")
print("Lista fordítása végéről kivett elemekkel: 1")
print("Lista fordítása helyben, elemeket cserélve: 2")
valasztas = int(input("Cserélési módszer? "))
if valasztas == 0:
  visszafele_forditott(eredeti)
elif valasztas == 1:
  vegerol_forditott(eredeti)
elif valasztas == 2:
  cserelo_forditott(eredeti)
else:
  print("Adj meg létező opciót.")
