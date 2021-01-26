#!/usr/bin/env python3

"""
| ALAP      | poz=0                  | " "                | "." | "?" | "!"      | egyéb                   |
|-----------|------------------------|--------------------|----------------------|-------------------------|
| ALAP      | m += c.upper(), ->ALAP | m+=c, - (ALAP)     | m+= c, ->PONT_VOLT   | m += c, - (ALAP)        |
| PONT_VOLT | m += c.upper(), ->ALAP | m+=c, - (PONT_VOLT)| m+= c, - (PONT_VOLT) | m += c.upper(), -> ALAP |
"""

import sys

def main():

    ALAP = 0
    PONT_VOLT = 1

    allapot = ALAP
    
    c = sys.stdin.read(1)
    m = ""
    while c != "": 
        if m == "": # Mondat (input) első karaktere
            m += c.upper()
            allapot = ALAP
        elif c == "." or c == "?" or c == "!":
            m += c
            allapot = PONT_VOLT
        elif c == " ": # Space-nél ne váltson állapotot
            m += c
        else:
            if allapot == ALAP:
                m += c
            else:
                m += c.upper()
                allapot = ALAP
        c = sys.stdin.read(1)

    print(m)
                


main()
