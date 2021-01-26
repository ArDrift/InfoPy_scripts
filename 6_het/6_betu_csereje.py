#!/usr/bin/env python3

def betucsere(szo, poz, betu):
  
  if poz not in range(0, len(szo)):
    raise ValueError("A '{}' számú index a megadótt szón kívülre esik.".format(poz))
  else:
  
    ujszo = ""
    
    for i in range(0, len(szo)):
      if i < poz:
        ujszo += szo[i]
      elif i == poz:
        ujszo += betu
      else:
        ujszo += szo[i]
      
    return ujszo


def main():
  try:
    print(betucsere("papa", 1, "i"))
  except ValueError as e:
    print("Érvénytelen pozíció:", e)

main()
