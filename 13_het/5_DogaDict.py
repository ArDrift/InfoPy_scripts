#!/usr/bin/env python3

def beolvas(file):
    with open(file, "rt") as f:
        dogadict = {}
        for sor in f:
            dogaadat = sor.rstrip("\n").split(":")
            dogadict[dogaadat[0]] = int(dogaadat[1])
    return dogadict


def pontdb(eredmenyek):
    pontdict = {}
    for pont in eredmenyek.values():
        pontdict[pont] = 0
        for neptun in eredmenyek:
            if eredmenyek[neptun] == pont:
                pontdict[pont] += 1
    return pontdict


def pontneptun(eredmenyek):
    neptunok = {}
    for pont in eredmenyek.values():
        neptunok[pont] = []
        for neptun in eredmenyek:
            if eredmenyek[neptun] == pont:
                neptunok[pont].append(neptun)
    return neptunok


def kiir_rendezett(szotar):
    for kulcs in sorted(szotar):
        print("{}: {}".format(kulcs, szotar[kulcs]))


def main():
    eredmenyek = beolvas("5_zheredmeny.txt")
    print("{} hallgató írta meg a dolgozatot.".format(len(eredmenyek)))
    
    pontdict = pontdb(eredmenyek)
    kiir_rendezett(pontdict)

    kiknek = pontneptun(eredmenyek)
    kiir_rendezett(kiknek)


main()
