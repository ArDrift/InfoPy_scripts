#!/usr/bin/env python3

size = int(input("Add meg a mezők méretét: "))

for i in range(4):
  for j in range(size):
    for k in range(4):
      print("X" * size, "." * size, sep="", end="")
    print("")

  for l in range(size):
    for m in range(4):
      print("." * size, "X" * size, sep="", end="")
    print("")
