#!/usr/bin/env python3

class Node:
    def __init__(self, valid=False, gyerek={}):
        self.valid = valid
        self.gyerek = gyerek


def betesz(szo, fa, poz=0):
    if poz < len(szo)-1:
        if fa.gyerek.get(szo[poz], -1) == -1:
            fa.gyerek[szo[poz]] = Node()
        betesz(szo, fa.gyerek[szo[poz]], poz+1)
    else:
        fa.valid = True
        if fa.gyerek.get(szo[poz], -1) == -1:
            fa.gyerek[szo[poz]] = Node()
        return "ok."


def keres(szo, fa, poz=0):
    if poz < len(szo) - 1:
        try:
            return keres(szo, fa.gyerek[szo[poz]], poz+1)
        except KeyError:
            return False
    else:
        return fa.valid and szo[poz] in fa.gyerek
     
"""
A Node-ot javítottam, sajnos a listázásba beletört a bicskám. Bíztató volt hogy az ötlet jó, de közben elvesztem a szótár + rekurzió kombóban :/

def listaz(fa, betuk="", poz=0):
    kulcsok = list(fa.gyerek)
    if fa.valid:
        print(betuk)
        return
    else:
        for elem in kulcsok:
            listaz(fa.gyerek[kulcsok[poz]], betuk+kulcsok[poz], poz+1)
"""
"""
def listaz(fa, kulcs, betuk=""):
    if fa.valid:
        print(betuk)
        return betuk
    else:
        for k in fa.gyerek:
            listaz(fa.gyerek[k], k, betuk+kulcs)
"""

def main():
    trie = Node()
    bemenet = input("")
    while bemenet != "kilep":
        parancs = bemenet.split(" ")[0]
        try:
            pmeter = bemenet.split(" ")[1]
        except IndexError as e:
            pass
        if parancs == "betesz":
            betesz(pmeter, trie)
            print("ok.")
        elif parancs == "keres":
            if keres(pmeter, trie):
                print("benne van.")
            else:
                print("nincs benne.")
#        elif parancs == "listaz":
#            for kulcs in trie.gyerek:
#                  listaz(trie, kulcs)
        bemenet = input("")


main()
