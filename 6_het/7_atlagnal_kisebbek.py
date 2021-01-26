#!/usr/bin/env python3

def atlag(szamlista):
  return sum(szamlista) / len(szamlista)


def szures(szamlista, szamatlag):
  szurt = []
  for i in szamlista:
    if i < szamatlag:
      szurt.append(i)

  return szurt


def main():
  szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]
  print(szures(szamok, atlag(szamok)))


main()
