#!/usr/bin/env python3

def main():
    keszlet = {
        "banán": 6,
        "alma": 31,
        "narancs": 32,
        "körte": 15
    }
     
    arak = {
        "banán": 100,
        "alma": 80,
        "narancs": 120,
        "körte": 90
    }

    print(sum([keszlet[x] * arak[x] for x in keszlet]))


main()
