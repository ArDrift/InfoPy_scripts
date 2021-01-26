#!/usr/bin/env python3

def main():

    vers = "Nem a régi s durva közelítés, / Mi szótól szóig így kijön / betűiket számlálva. / Ludolph eredménye már, / ha itt végezzük húsz jegyen. / De rendre kijő még tíz pontosan, / azt is bízvást ígérhetem."

    szamjegyek = [print(len(s.strip(",.")), end="") for s in vers.split(" ") if s != "/"]


main()
