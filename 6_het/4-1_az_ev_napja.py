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


def main():
  honap = int(input("Add meg a hónap számát: "))
  print(honap_napszam(honap))
  return


main()
