#!/usr/bin/env python3

import math

def szamrendszerbol(szamstr, rendszer):
  res = 0
  for b in range(len(szamstr)):
    if szamstr[b].isdecimal():
      res += int(szamstr[b]) * rendszer ** (len(szamstr) - 1 - b)
    else:
      if ord(szamstr[b].upper()) - 65 <= rendszer - 11:
        res += (ord(szamstr[b].upper())-55) * rendszer ** (len(szamstr) - 1 - b)
      else:
        raise ValueError("A megadott számrendszerben '{}' nem létezik.".format(szamstr[b]))

  return res


def szamrendszerbe(szam, rendszer):
  if rendszer > 1:
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
            res.append(chr(65 + szam//hertek -10).lower())
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
        return chr(65 + abs(szam)-10).lower()
  else:
    raise ValueError("Nem lehetséges az adott ({}) számrendszerbe való konvertálás.".format(rendszer))


def main():
  print(szamrendszerbol("a20", 16))
  print(szamrendszerbe(420, 2))


main()
