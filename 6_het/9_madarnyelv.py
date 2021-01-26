#!/usr/bin/env python3

def is_vowel(ltr):
  return ltr == 'a' or ltr == 'e' or ltr == 'i' or ltr == 'o' or ltr == 'u'


def madarnyelv(text):
  newtext = ""
  for c in text:
    if is_vowel(c.lower()):
      newtext += c + 'v' + c.lower()
    else:
      newtext += c

  return newtext


def main():
  print(madarnyelv("Elmegyek enni"))


main()
