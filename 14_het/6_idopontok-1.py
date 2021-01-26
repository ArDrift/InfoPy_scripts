#!/usr/bin/env python3

import re

def main():

    elso = r"^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$"
    masodik = r"^[0-2][0-9]h [0-5][0-9]m [0-5][0-9]s$"
    harmadik = r"^[0-1][0-2]:[0-5][0-9] AM|PM$"
    
    ido = input("Add meg az időpontot: ")    
    while ido != "":
        if re.search(elso, ido):
            print("Első formátum")
        elif re.search(masodik, ido):
            print("Második formátum")
        elif re.search(harmadik, ido):
            print("Harmadik formátum")
        else:
            print("Hibás")
        ido = input("Add meg az időpontot: ")    


main()
