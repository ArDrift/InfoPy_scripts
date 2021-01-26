#!/usr/bin/env python3

szamok = [2.5, -69, 5.4, -8, -7.7, 6, 2.9, -10, -3, 9.8]
negativak = []

for elem in range(0, len(szamok)):
  print("[{}] = {}".format(elem, szamok[elem]))
  
  if szamok[elem] < 0:
    negativak.append(elem)
    
print("Ebből {} szám negatív.".format(len(negativak)))

for index in range(len(negativak)):
  print("{}. [{}] = {}".format(index + 1, negativak[index], szamok[negativak[index]]))

