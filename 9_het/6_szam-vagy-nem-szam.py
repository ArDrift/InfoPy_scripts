#!/usr/bin/env python3

def szam_e(a):
  try:
    int(a)
    return True
  except:
    return False


def main():
  print(szam_e("123"))


main()
