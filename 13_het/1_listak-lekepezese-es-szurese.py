#!/usr/bin/env python3

def main():
    #a)
    l = [i*2 for i in range(0, 10)]

    #b)
    l = [i for i in range(100) if i % 10 == 3]

    #c)
    l1 = [43, 15, 48, 59, 33, 72, 11, 65, 95, 34]
    l2 = [i for i in l1 if i % 2 == 1]

    #d)
    l1 = [43, 15, 48, 59, 33, 72, 11, 65, 95, 34]
    l2 = [i % 2 == 1 for i in l1]

    #e)
    l1 = ["alma", "körte", "barack", "szilva", "ananász"]
    l2 = [s for s in l1 if s[0] == "a"]

    #f)
    l1 = ["alma", "körte", "barack", "szilva", "meggy"]
    l2 = [len(s) for s in l1]

    print(l2)


main()
