#!/usr/bin/env python3

def hatvanyozas(alap, kitevo):
  if kitevo == 0:
    return 1
  elif kitevo == 1:
    return alap
  else:
    if kitevo % 2 == 0:
      return hatvanyozas(alap, kitevo // 2) * hatvanyozas(alap, kitevo // 2)
    else:
      return hatvanyozas(alap, kitevo - 1) * alap


def main():
  for i in range(0, 16):
    print("2^{:<2} = {:>5}".format(i, hatvanyozas(2, i)))


main()
