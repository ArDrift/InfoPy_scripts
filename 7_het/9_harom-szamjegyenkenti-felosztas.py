#!/usr/bin/env python3

def harmasosztas(szam):
  if szam in range(0, 10):
    return "00" + str(szam)
  elif szam in range(10, 100):
    return "0" + str(szam)
  elif szam in range(100, 1000):
    return szam
  else:
    return str(harmasosztas(szam // 1000)) + " " + str(harmasosztas(szam % 1000))


def main():
  print(harmasosztas(1000222))


main()
