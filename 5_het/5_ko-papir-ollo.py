#!/usr/bin/env python3

import random

print("Kő (k), papír (p), olló (o) vagy vége (v)? ")

result = ""
points = 0

comppoints = 0
choice = input("Szerinted: ")

while choice != "v":

  compchoice = random.choice(["k", "p", "o"])

  print("Szerintem:", compchoice)

  if choice == compchoice:
    result = "Senki nem kap pontot." + "\n"

  elif choice == "k" and compchoice == "p":
    result = "k<p, ezt én vittem!" + "\n"
    comppoints += 1
  elif choice == "k" and compchoice == "o":
    result = "k>o, ezt te vitted!" + "\n"
    points += 1

  elif choice == "p" and compchoice == "k":
    result = "k>p, ezt te vitted!" + "\n"
    points += 1
  elif choice == "p" and compchoice == "o":
    result = "p<o, ezt én vittem!" + "\n"
    comppoints += 1

  elif choice == "o" and compchoice == "k":
    result = "o<k, ezt én vittem!" + "\n"
    comppoints += 1
  elif choice == "o" and compchoice == "p":
    result = "o>p, ezt te vitted!" + "\n"
    points += 1

  print(result)
  choice = input("Szerinted: ")


if points == comppoints:
  print("Döntetlen.")
elif points > comppoints:
  print("Te nyertél, {}>{} ponttal".format(points, comppoints))
else:
  print("Én nyertem, {}<{} ponttal".format(points, comppoints))
