#!/usr/bin/env python3

class BinFa:
    def __init__(self, ertek):
        self.ertek = ertek
        self.bal = None
        self.jobb = None


def epit(gyoker, adat):
    if gyoker is None:
        gyoker = BinFa(adat)
    elif adat < gyoker.ertek:
        gyoker.bal = epit(gyoker.bal, adat)
    elif adat > gyoker.ertek:
        gyoker.jobb = epit(gyoker.jobb, adat)
    
    return gyoker


def inorder(gyoker):
    if gyoker is None:
        return
    
    inorder(gyoker.bal)
    print(gyoker.ertek)
    inorder(gyoker.jobb)


def elemszam(gyoker):
    if gyoker is None:
        return 0
    
    return (elemszam(gyoker.bal) + elemszam(gyoker.jobb) + 1)


def szumma(gyoker):
    if gyoker is None:
        return 0
    
    return (szumma(gyoker.bal) + szumma(gyoker.jobb) + gyoker.ertek)


def keres(gyoker, keresett):
    if gyoker is None:
        return
    elif keresett > gyoker.ertek:
        return keres(gyoker.jobb, keresett)
    elif keresett < gyoker.ertek:
        return keres(gyoker.bal, keresett)
    else:
        return gyoker


def magassag(gyoker):
    if gyoker is None:
        return 0
    elif magassag(gyoker.bal) > magassag(gyoker.jobb):
        return (magassag(gyoker.bal) + 1)
    else:
        return (magassag(gyoker.jobb) + 1)


def main():
    tesztadat = [15, 96, 34, 12, 14, 56, 21, 11, 10, 9, 78, 43]
    gyoker = None
    for x in tesztadat:
        gyoker = epit(gyoker, x)
        
    print(magassag(gyoker))
 
 
main()

