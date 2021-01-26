#!/usr/bin/env python3

lista = [-25, 12, -54, 8, 77, 98, -29, 35, 3, 71]
maximum = lista[0]

print("Korábbi legnagyobb:", maximum)
for elem in range(1, len(lista)):
  print("Vizsgált elem:", lista[elem])
  if lista[elem] > maximum:
    maximum = lista[elem]
    print("Aktuális legnagyobb:", maximum)

    
print("Végső legnagyobb:", maximum)

