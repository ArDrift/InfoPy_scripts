#!/usr/bin/env python3

import sys

# 2.)
# Mert a program először bemenetre vár,
# de először csak 1 karaktert fog beolvasni.
# Utána a while ciklus file vége jelig fut, viszont ha elfogyott a bemenet,
# újabb bemenetre fog várni.
# 3.)
# Linuxon Ctrl+D-vel. 
# 4.)
# A 10-es karakterkód entert jelent.

def main():
    karakter = sys.stdin.read(1)
    while karakter != "":
        print(ord(karakter))
        karakter = sys.stdin.read(1)
    print("Bemenet vége.")


main()
