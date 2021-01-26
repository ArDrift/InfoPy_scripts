#!/usr/bin/env python3

def main():
    fagyik = {
        "pisztácia": 0,
        "vanília": 3,
        "tutti-frutti": 8,
        "karamell": 4,
        "rumos dió": 5,
        "kávé": 9,
    }

    iz = input("Fagyi? ")
    while iz != "":
        valasz = fagyik.get(iz, -1)
        if valasz == -1:
            print("{} nem is volt!".format(iz))
        elif valasz == 0:
            print("{} kifogyott!".format(iz))
        else:
            print("kösz, öcsi!")
            fagyik[iz] -= 1
        iz = input("Fagyi? ")
    return
    

main()    
