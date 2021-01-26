#!/usr/bin/env python3

import math

def kob(a):
  return a ** 3


def abszolut(a):
  if a < 0:
    return a * -1
  else:
    return a


def main():
  a = -1.0
  while a < 1:
    print("{:8.4f} {:8.4f} {:8.4f} {:8.4f}".format(a, kob(a), abszolut(a), math.sin(a)))
    a += 0.1
  return


main()
