#!/usr/bin/env python3

def szokoev_e(ev):
  return ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0)
  
  
def main():
  evszam = int(input("Add meg az évszámot: ")) 
  if szokoev_e(evszam):
    print("Szökőév.")
  else:
    print("Nem szökőév.")


main()
