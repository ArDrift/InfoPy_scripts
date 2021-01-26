#!/usr/bin/env python3

"""
A megoldás elkészítéséhez felhasználtam a következő forrásokat:
https://docs.python.org/3/library/stdtypes.html
"""

import random

text = input("Add meg a keverendő szöveget: ").split()
mixed_list = []
mixed_text = ""

for word in text:
  text_list = []
  punct_length = 0
  for char in word:
    text_list.append(char)
    if char.upper() == char.lower():
      punct_length += 1

  mixed_list.append(text_list.pop(0))
  if len(word) + punct_length > 2:
    for elem in range(1, len(word) - 1 - punct_length):
      mixed_list.append(text_list.pop(random.randint(0, len(text_list) - 2 - punct_length)))

  if len(word) + punct_length > 1:
    mixed_list.append(text_list.pop(-1 - punct_length))

  for char in range(punct_length):
    mixed_list.append(text_list.pop(0))

  mixed_list.append(" ")

for elem in mixed_list:
  mixed_text += elem

print("\n" + mixed_text)
