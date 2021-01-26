#!/usr/bin/env python3

def atvalt(szam, szamr):
  if szam < szamr:
    return szam
  else:
    return str(atvalt(szam // szamr, szamr)) + str(atvalt(szam % szamr, szamr))


def main():
  print(atvalt(42, 2))


main()
