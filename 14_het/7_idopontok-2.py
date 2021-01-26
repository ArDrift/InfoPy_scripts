#!/usr/bin/env python3

import re

class Idopont():
    def __init__(self, ora, perc, mp=0):
        self.ora = ora
        self.perc = perc
        self.mp = mp


    def __str__(self):
        return "{}ó {}p {}mp".format(self.ora, self.perc, self.mp)


def match_format(ido):
    elso = r"^([0-2][0-9]):([0-5][0-9]):([0-5][0-9])$"
    masodik = r"^([0-2][0-9])h ([0-5][0-9])m ([0-5][0-9])s$"
    harmadik = r"^([0-1][0-9]):([0-5][0-9]) (A|P)M$"

    if re.search(elso, ido):
        return re.search(elso, ido)
    
    elif re.search(masodik, ido):
        return re.search(masodik, ido)
    
    elif re.search(harmadik, ido):
        return re.search(harmadik, ido)


def make_idopont(ido):
    res = match_format(ido)
    if res.group(3) != "A" and res.group(3) != "P":
        return Idopont(res.group(1), res.group(2), res.group(3))
    else:
        if res.group(3) == "A":
            return Idopont(res.group(1), res.group(2))
        else:
            return Idopont(int(res.group(1))+12, res.group(2))


def main():

    elso = r"^([0-2][0-9]):([0-5][0-9]):([0-5][0-9])$"
    masodik = r"^([0-2][0-9])h ([0-5][0-9])m ([0-5][0-9])s$"
    harmadik = r"^([0-1][0-9]):([0-5][0-9]) (A|P)M$"

    ido = input("Add meg az időpontot: ")    
    while ido != "":
        if re.search(elso, ido):
            res = re.search(elso, ido)
            print("{}ó {}p {}mp".format(res.group(1), res.group(2), res.group(3)))
        elif re.search(masodik, ido):
            res = re.search(masodik, ido)
            print("{}ó {}p {}mp".format(res.group(1), res.group(2), res.group(3)))
        elif re.search(harmadik, ido):
            res = re.search(harmadik, ido)
            print(res)
            print("{}ó {}p {}".format(res.group(1), res.group(2), res.group(3)))
        else:
            print("Hibás")
        ido = input("Add meg az időpontot: ")    

    
    print(make_idopont("09:34 PM"))


main()
