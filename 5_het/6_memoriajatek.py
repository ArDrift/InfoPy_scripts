#!/usr/bin/env python3

import random

viscards = []

for code in range(65, 65+18):
  viscards.append(chr(code))
  viscards.append(chr(code))
  

for elem in range(0, len(viscards) - 1):
  temp = viscards[elem]
  randindex = random.choice(range(0, len(viscards) - 1))
  viscards[elem] = viscards[randindex]
  viscards[randindex] = temp


for _ in range(0, 6):
  for _ in range(0, 6):
    print("X ", end="")
  print("")
  
print("-" * 11)

choice = int(input("Válassz koordinátát balról jobbra, fentről le: 1 - 36: "))

while choice != 0:


  for x in range(0, 6):
    for y in range(0, 6):
      if y + 6*x != choice - 1:
        print("X ", end="")
      else:
        print(viscards[choice - 1], "", end="")
    print("")
    
  newchoice = int(input("Találd meg a párját (1 - 36): "))


  for x in range(0, 6):
    for y in range(0, 6):
      if y + 6*x == choice - 1:
        print(viscards[choice - 1], "", end="")
      elif y + 6*x == newchoice - 1:
        print(viscards[newchoice - 1], "", end="")
      else:
        print("X ", end="")
        
    print("")
    
  if viscards[choice - 1] == viscards[newchoice - 1]:
    print("Találat, nyertél!")
  else:
    print("Vesztettél!")

  print("-" * 11)

  choice = int(input("Válassz koordinátát balról jobbra, fentről le: 1 - 36: "))
