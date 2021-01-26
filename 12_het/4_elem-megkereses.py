#!/usr/bin/env python3

class BinFa:
    def __init__(self, ertek):
        self.ertek = ertek
        self.bal = None
        self.jobb = None
 
 
def beszur(gyoker, ertek):
    if gyoker is None:
        gyoker = BinFa(ertek)
    elif ertek < gyoker.ertek:
        gyoker.bal = beszur(gyoker.bal, ertek)
    elif ertek > gyoker.ertek:
        gyoker.jobb = beszur(gyoker.jobb, ertek)
    else:
        pass
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


def main():
    tesztadat = [15, 96, 34, 12, 14, 56, 21, 11, 10, 9, 78, 43]
    gyoker = None
    for x in tesztadat:
        gyoker = beszur(gyoker, x)
        
    print(keres(gyoker, 12))
 
 
main()

