#!/usr/bin/env python3

print("Írj be szavakat, majd jelezd üres sorral a lista végét!")
szo = input()
szolista = []
szolista.append(szo)

while szo:
  szo = input()
  szolista.append(szo)

szolista.pop()

print("A beírt szavak: ", end="")

for elem in range(len(szolista)):
  print(szolista[elem], end="")
  if elem != len(szolista) - 1:
    print(", ", end="")
  else:
    print(".")
