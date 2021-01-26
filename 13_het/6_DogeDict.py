#!/usr/bin/env python3

class Doge:
    def __init__(self, az, nev, papa=-1, mama=-1):
        self.az = az
        self.nev = nev
        self.papa = papa
        self.mama = mama
    
    
    def __str__(self):
        return "{} {} {} {}".format(self.az, self.nev, self.papa, self.mama)
        

def kiir_ossz(szotar):
    for kulcs in szotar:
        print("{}: {}".format(kulcs, szotar[kulcs].nev))
    

def keres(szotar, az):
    return szotar.get(az, None)


def torol(szotar, az):
    for elem in szotar:
        if szotar[elem].mama == az:
            szotar[elem].mama = -1
        if szotar[elem].papa == az:
            szotar[elem].papa = -1
    szotar.pop(az)


def kiir_file(szotar, file):
    with open(file, "wt") as f:
        for elem in szotar:
            print(szotar[elem], file=f)


def beolvas(file):
    result = {}
    with open(file, "rt") as f:
        for sor in f:
            adatok = sor.rstrip("\n").split(" ")
            result[adatok[0]] = Doge(adatok[0], adatok[1], adatok[2], adatok[3])

    return result


def main():
    doges = {}
    doges[5] = Doge(5, "Woof")
    doges[7] = Doge(7, "Floof")
    doges[6] = Doge(6, "Fluff", 5, 7)
        
    kiir_ossz(doges)
    dogeid = input("Add meg a kutya azonosítóját: ")
    while dogeid != "":
        try:
            print(keres(doges, int(dogeid)))
        except ValueError as e:
            print("Kérlek számot adj meg!")
        dogeid = input("Add meg a kutya azonosítóját: ")
        
    kiir_file(doges, "6_doges.txt")
    uj = beolvas("6_new-doges.txt")
    for kutya in uj:
        print(uj[kutya])


main()
