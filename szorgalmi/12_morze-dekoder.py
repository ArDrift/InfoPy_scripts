#!/usr/bin/env python3

class BinFa:
    def __init__(self, adat):
        self.adat = adat
        self.bal = None
        self.jobb = None


def epit(gyoker, adat, betu, poz=0):
    if gyoker is None:
        gyoker = BinFa(None)
    if poz <= len(adat) - 1:
        if adat[poz] == ".":
            gyoker.bal = epit(gyoker.bal, adat, betu, poz+1)
        else:
            gyoker.jobb = epit(gyoker.jobb, adat, betu, poz+1)
    else:
        gyoker.adat = betu

    return gyoker


def morse_decode(jelsor, gyoker, poz=0):
    if poz == len(jelsor):
        return gyoker.adat
    elif jelsor[poz] == ".":
        return morse_decode(jelsor, gyoker.bal, poz+1)
    elif jelsor[poz] == "-":
        return morse_decode(jelsor, gyoker.jobb, poz+1)


def main():
    morseabc = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."]
            
    morsegyoker = None
    for i in range(len(morseabc)):
        betu = chr(65 + i)
        morsegyoker = epit(morsegyoker, morseabc[i], betu)
    
    mondat = ""
    with open("morze.txt", "rt") as f:
        for sor in f:
            szo = ""
            for betu in sor.rstrip("\n").split(" "):
                szo += morse_decode(betu, morsegyoker)
            mondat += szo + " "
            
    print(mondat)


main()
