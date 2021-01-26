#!/usr/bin/env python3

import sys

"""
Áll.\Vált. |    L betű         |          l betű       |     y betű       |      Egyéb        |
-----------|-------------------|-----------------------|------------------|-------------------|
   ALAP    | ->N_L_VOLT        |        ->L_VOLT       | sz+=c, - (ALAP)  | sz+=c, - (ALAP)   |
  L_VOLT   | sz+="l",->N_L_VOLT|        ->LL_VOLT      | sz+="j",->ALAP   | sz+="l"+c,->ALAP  |
  LL_VOLT  |sz+="ll",->N_L_VOLT| sz+="ll", - (LL_VOLT) | sz+="jj",->ALAP  | sz+="ll"+c,->ALAP |
  N_L_VOLT |  sz+="L", -       |       -> N_LL_VOLT    | sz+="J", ->ALAP  | sz+="L"+c,->ALAP  |
 N_LL_VOLT |  sz+="Ll", -      |    sz+="L",->LL_VOLT  | sz+="Jj", ->ALAP | sz+="Ll"+c,->ALAP |
"""


def main():
    ALAP = 1
    L_VOLT = 2
    LL_VOLT = 3
    N_L_VOLT = 4
    N_LL_VOLT = 5
    
    szo = ""
    allapot = ALAP
    
    while True:
        c = sys.stdin.read(1)
        if c == "":
            break
        
        if allapot == ALAP:      # szöveg kezdete
            if c == "L":
                allapot = N_L_VOLT
            elif c == "l":
                allapot = L_VOLT
            else:
                szo += c
        
        elif allapot == L_VOLT:  # már volt egy l
            if c == "L":
                szo += "l"
                allapot = N_L_VOLT
            elif c == "l":
                allapot = LL_VOLT
            elif c == "y":
                szo += "j"
                allapot = ALAP
            else:
                szo += "l" + c
                allapot = ALAP
        
        elif allapot == LL_VOLT: # két l volt
            if c == "L":
                szo += "ll"
                allapot = N_L_VOLT
            elif c == "l":
                szo += "ll"
            elif c == "y":
                szo += "jj"
                allapot = ALAP
            else:
                szo += "ll" + c
                allapot = ALAP
                
        elif allapot == N_L_VOLT: # nagy L volt
            if c == "L":
                szo += "L"
            elif c == "l":
                allapot = N_LL_VOLT
            elif c == "y":
                szo += "J"
                allapot = ALAP
            else:
                szo += "L" + c
                allapot = ALAP

        elif allapot == N_LL_VOLT: # Ll volt
            if c == "L":
                szo += "Ll"
            elif c == "l":
                szo += "L"
                allapot = LL_VOLT
            elif c == "y":
                szo += "Jj"
                allapot = ALAP
            else:
                szo += "Ll" + c
                allapot = ALAP
 
    print(szo)
 
main()

