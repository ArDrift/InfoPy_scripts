#!/usr/bin/env python3

def szamtani(first=None, second=None, third=None):
  if first is None:
    raise TypeError("A maximumot muszáj megadni!")
  else:
    max = first
    if second is None:
      min = 0
    else:
      min = first
      max = second
    if third is None:
      step = 1
    else:
      step = third

    tag = min
    if step > 0:
      while tag < max:
        if tag < max - step:
          print(tag, ", ", end="", sep="")
        else:
          print(tag)
        tag += step
    elif step < 0:
      while tag > max:
          if tag > max - step:
            print(tag, ", ", end="", sep="")
          else:
            print(tag)
          tag += step
    else:
      raise ValueError("A 0 lépésszámú sorozat végtelen elemű!")

def main():
  try:
    szamtani(3)
  except TypeError as e:
    print(e)
    return
  except ValueError as e:
    print(e)
    return


main()
