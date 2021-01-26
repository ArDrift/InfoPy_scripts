#!/usr/bin/env python3

def honap_napszam(hoszam):
  napszam = 0
  if (hoszam < 8 and hoszam % 2 == 1) or (hoszam >= 8 and hoszam % 2 == 0):
    napszam = 31
  elif hoszam == 2:
    napszam = 28
  else:
    napszam = 30
  return napszam


def evnapja(ev, honap, nap):
  napsorszam = 0
  for ho in range(honap - 1, 0, -1):
    napsorszam += honap_napszam(ho)
    
  napsorszam += nap
  
  if szokoev_e(ev) and honap > 2:
    napsorszam += 1
  
  return napsorszam


def szokoev_e(ev):
  return ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0)


def main():
  napszam = int(input("Add meg a nap számát: "))
  honapszam = int(input("Add meg a hónap számát: "))
  evszam = int(input("Add meg az év számát: "))
  
  print(evnapja(evszam, honapszam, napszam))
  return


main()
