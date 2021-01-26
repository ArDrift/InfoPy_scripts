#!/usr/bin/env python3

def pontbe():
  pont = int(input("Add meg a pontot: "))
  if pont < 0 or pont > 10:
    raise ValueError
  return pont


def be_cont():
  pontlista = []
  
  while True:
    try:
      pontlista.append(pontbe())
    except ValueError:
      return pontlista
  
  return pontlista


def vanmax(lista):
  for elem in lista:
    if elem == 10:
      return True

  return False


def main():
  if vanmax(be_cont()):
    print("Lett maximum pontos")
  else:
    print("Nem lett maximum pontos")


main()
