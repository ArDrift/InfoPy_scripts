#!/usr/bin/env python3

betulista = ["P", "i", "t", "a", "g", "o", "r", "a", "s", "z"]
cserelendo = ""

for sor in range(11):
  cserelendo = betulista[0]
  for betu in range(len(betulista)):
    print(betulista[betu], end="")
    if betu != len(betulista) - 1:
      print(" ", end="")
  print("")
  # elem 0 tól 9ig
  for elem in range(len(betulista)):
    if elem < len(betulista) - 1:
      betulista[elem] = betulista[elem + 1]
    else:
      betulista[elem] = cserelendo
