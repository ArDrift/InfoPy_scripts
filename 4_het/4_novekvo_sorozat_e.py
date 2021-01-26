#!/usr/bin/env python3

# Eldöntés tétele

jo_lista = [1, 2, 3, 4, 5, 6, 7, 8]
a_lista = [1, 2, 0, 3, -1, -10, 10, 20]
b_lista = [1, 2, 3, -5, 6, 7, 8, 9]
c_lista = [10, 1, 2, 3, 4, 5, 6, 7]
d_lista = [1, 2, 3, 4, 5, 6, 7, -10]

rendezett = False

def rendezett_e(lista):
  for elem in range(0, len(lista) - 1):
    if lista[elem + 1] > lista[elem]:
      rendezett = True
    else:
      rendezett = False
      break
    
  if rendezett == True:
    print("A lista rendezett.")
  else:
    print("A lista nem rendezett.")
    
rendezett_e(jo_lista)
