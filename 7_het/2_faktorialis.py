#!/usr/bin/env python3

def faktor(szam):
  if szam == 0:
    return 1
  else:
    return szam * faktor(szam - 1)


def main():
  for i in range(10 + 1):
    print("{}! = {}".format(i, faktor(i)))
  
  return


main()
