#!/usr/bin/env python3

import sys

"""
Áll.\Vált. |   L betű    |   Y betű    |   Egyéb  |
-----------|-------------|-------------|----------|
   ALAP    |  ->L_VOLT   |  - (ALAP)   | - (ALAP) |
  L_VOLT   |  ->LL_VOLT  | sz+1,->ALAP |  ->ALAP  |
  LL_VOLT  | - (LL_VOLT) | sz+2,->ALAP |  ->ALAP  |

"""


def main():
    ALAP = 1
    L_VOLT = 2
    LL_VOLT = 3
    
    szaml = 0
    allapot = ALAP
    
    while True:
        c = sys.stdin.read(1)
        if c == "":
            break
        
        if allapot == ALAP:      # szöveg kezdete
            if c == "l":
                allapot = L_VOLT
        
        elif allapot == L_VOLT:  # már volt egy l
            if c == "l":
                allapot = LL_VOLT
            elif c == "y":
                szaml += 1
                allapot = ALAP
            else:
                allapot = ALAP
        
        elif allapot == LL_VOLT: # két l volt
            if c == "l":
                pass
            elif c == "y":
                szaml += 2
                allapot = ALAP
            else:
                allapot = ALAP
 
    print(szaml, "darab ly volt.")
 
main()

