#!/usr/bin/env python3

class BinFa:
    def __init__(self, adat):
        self.adat = adat
        self.jobb = None
        self.bal = None


    def __str__(self):
        if self.adat == Kifejezes.szorzas:
            return "({} * {})".format(self.bal, self.jobb)
        elif self.adat == Kifejezes.osszeadas:
            return "({} + {})".format(self.bal, self.jobb)
        else:
            return str(self.adat)


class Kifejezes:
    szorzas = "*"
    osszeadas = "+"


def kiertekel(gyoker, valtozo):
    if gyoker.adat == Kifejezes.szorzas:
        return kiertekel(gyoker.bal, valtozo) * kiertekel(gyoker.jobb, valtozo)
    elif gyoker.adat == Kifejezes.osszeadas:
        return kiertekel(gyoker.bal, valtozo) + kiertekel(gyoker.jobb, valtozo)
    elif gyoker.adat == "x":
        return valtozo
    else:
        return gyoker.adat


def main():
    gyoker = BinFa(Kifejezes.szorzas)
    gyoker.jobb = BinFa(8)
    gyoker.bal = BinFa(Kifejezes.osszeadas)
    gyoker.bal.bal = BinFa(3)
    gyoker.bal.jobb = BinFa("x")

    print(gyoker)
    print("={}".format(kiertekel(gyoker, 2)))


main()
