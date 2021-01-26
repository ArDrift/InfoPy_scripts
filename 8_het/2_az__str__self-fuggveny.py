#!/usr/bin/env python3

class Datum:
    def __init__(self, ev, honap, nap):
        self.ev = ev
        self.honap = honap
        self.nap = nap


    def __str__(self):
        return "{}.{:0>2}.{:0>2}".format(self.ev, self.honap, self.nap) 

 
class Versenyzo:
    def __init__(self, nev, szuletes, helyezes):
        self.nev = nev
        self.szuletes = szuletes
        self.helyezes = helyezes
 

    def __str__(self):
        return ("Név: {}, született: {}, helyezés: {}.".format(self.nev, self.szuletes, self.helyezes))


def main():
    versenyzok = [
        Versenyzo("Am Erika", Datum(1994, 5, 6), 1),
        Versenyzo("Break Elek", Datum(2001, 9, 30), 3),
        Versenyzo("Dil Emma", Datum(1998, 8, 25), 2),
        Versenyzo("Kasza Blanka", Datum(1989, 6, 10), 5),
        Versenyzo("Reset Elek", Datum(2001, 4, 5), 4),
    ];
 
    print(versenyzok[0].nev)
    print(versenyzok[2].helyezes)
    print(versenyzok[4].szuletes)
    print(versenyzok[1].nev[0])
    if versenyzok[1].helyezes <= 3:
      print("igen")
    else:
      print("nem")
    print(versenyzok[4].helyezes < versenyzok[3].helyezes)
    print(versenyzok[1].szuletes.ev == versenyzok[2].szuletes.ev)
    print(versenyzok[1])
    for v in versenyzok:
      print(v)

 
main()
