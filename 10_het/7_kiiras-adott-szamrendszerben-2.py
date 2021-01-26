#!/usr/bin/env python3

import math

def atvalt(szam, rendszer):
  if abs(szam) > rendszer - 1:
    res = []
    resstr = ""
    if szam < 0:
      resstr += ("-")
      szam = abs(szam)
    pwc = math.floor(math.log(szam, rendszer))
    while szam > rendszer-1 or pwc >= 0:
      hertek = rendszer ** pwc
      if szam >= hertek:
        if szam // hertek >= 10:
          res.append(chr(65 + szam//hertek -10))
        else:
          res.append(szam // hertek)
        szam = szam - (szam // hertek) * rendszer ** pwc
      else:
        res.append(0)
      pwc -= 1
      
    for elem in res:
      resstr += str(elem)
    return resstr
        
  else:
    if abs(szam) < 10:
      return szam
    else:
      return chr(65 + abs(szam)-10)


def main():
  szam = -42
  print(atvalt(szam, 2))


main()
