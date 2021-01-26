#!/usr/bin/env python3

def a_kezdo(stringlist):
  for string in stringlist:
    if string != "":
      if string[0] == "a":
        return True
  
  return False


def main():
  lista = ["dinnye", "papaja", "", "zeller"]
  print(lista)

  if a_kezdo(lista):
    print("Van 'a' kezdőbetűs szó.")
  else:
    print("Nincs 'a' kezdőbetűs szó.")


main()
