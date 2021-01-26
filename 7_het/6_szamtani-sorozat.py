#!/usr/bin/env python3

def sorozat(elso, incr, sorszam):
  if sorszam == 0:
    return elso
  else:
    return sorozat(elso, incr, sorszam - 1) + incr
  

def main():
  for i in range(10 + 1):
    print(sorozat(0, 12, i), end=" ")
    
  print("")


main()
