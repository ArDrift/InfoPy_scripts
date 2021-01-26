#!/usr/bin/env python3

def main():
    keszlet = {
        "banán": 6,
        "alma": 31,
        "narancs": 32,
        "körte": 15
    }
     
    arak = {
        "banán": 100,
        "alma": 80,
        "narancs": 120,
        "körte": 90
    }

    zoldseg = input("")
    szumma = 0
    while zoldseg != "":
        db = keszlet.get(zoldseg, -1)
        if db <= 0:
            print("Nincs raktáron.")
        else:
            print("OK")
            keszlet[zoldseg] -= 1
            szumma += arak[zoldseg]
        zoldseg = input("")

    print("Végösszeg: {}".format(szumma))
    
    
main()
