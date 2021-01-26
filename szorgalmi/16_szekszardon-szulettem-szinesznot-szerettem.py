#!/usr/bin/env python3

import sys

"""
| Áll\Vált.   | nem betű              | "s" or "S"    | "z"           | egyéb         |
| ----------- | --------------------- | ------------- | ------------- | ------------- |
| STDIN_ELEJE | ->SZOHAT_VOLT         | ->S_KEZD      | ->ALAP        | ->ALAP        |
| ALAP        | ->SZOHAT_VOLT         | - (ALAP)      | - (ALAP)      | - (ALAP)      |
| SZOHAT_VOLT | - (SZOHAT_VOLT)       | ->S_KEZD      | ->ALAP        | ->ALAP        |
| S_KEZD      | ->SZOHAT_VOLT         | ->ALAP        | ->SZ_KEZD     | ->ALAP        |
| SZ_KEZD     | sz+= 1, ->SZOHAT_VOLT | sz+=1, ->ALAP | sz+=1, ->ALAP | sz+=1, ->ALAP |
"""

def main():
    sz = 0

    ALAP = 0
    SZOHAT_VOLT = 1
    S_KEZD = 2
    SZ_KEZD = 3
    STDIN_ELEJE = 4

    allapot = STDIN_ELEJE

    c = sys.stdin.read(1)

    while c != "":
        # nem betű, szóhatároló
        if not c.isalpha():
            if allapot == SZ_KEZD:
                sz += 1
            allapot = SZOHAT_VOLT

        elif c == "s" or c == "S":
            if allapot == STDIN_ELEJE or allapot == SZOHAT_VOLT:
                allapot = S_KEZD

            else:
                if allapot == SZ_KEZD:
                    sz += 1
                allapot = ALAP

        elif c == "z":
            if allapot == S_KEZD:
                allapot = SZ_KEZD

            else:
                if allapot == SZ_KEZD:
                    sz += 1
                allapot = ALAP

        else:
            if allapot == SZ_KEZD:
                sz += 1
            allapot = ALAP
            
        c = sys.stdin.read(1)

    print("{} db 'sz' betűvel kezdődő szó volt.".format(sz))


main()
