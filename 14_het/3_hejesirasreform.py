#!/usr/bin/env python3

import sys

"""
Áll.\Vált. |          L betű       |     Y betű       |      Egyéb        |
-----------|-----------------------|------------------|-------------------|
   ALAP    |        ->L_VOLT       | sz+=c, - (ALAP)  | sz+=c, - (ALAP)   |
  L_VOLT   |        ->LL_VOLT      | sz+="j",->ALAP   | sz+="l"+c,->ALAP  |
  LL_VOLT  | sz+="ll", - (LL_VOLT) | sz+="jj",->ALAP  | sz+="ll"+c,->ALAP |

"""


def main():
    ALAP = 1
    L_VOLT = 2
    LL_VOLT = 3
    
    szo = ""
    allapot = ALAP
    
    while True:
        c = sys.stdin.read(1)
        if c == "":
            break
        
        if allapot == ALAP:      # szöveg kezdete
            if c == "l":
                allapot = L_VOLT
            else:
                szo += c
        
        elif allapot == L_VOLT:  # már volt egy l
            if c == "l":
                allapot = LL_VOLT
            elif c == "y":
                szo += "j"
                allapot = ALAP
            else:
                szo += "l"+c
                allapot = ALAP
        
        elif allapot == LL_VOLT: # két l volt
            if c == "l":
                szo += "ll"
            elif c == "y":
                szo += "jj"
                allapot = ALAP
            else:
                szo += "ll"+c
                allapot = ALAP
 
    print(szo)
 
main()

