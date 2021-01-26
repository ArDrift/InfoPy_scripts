#!/usr/bin/env python3

import math

print("Másodfokú egyenlet")

a = float(input("Add meg a-t:"))
b = float(input("Add meg b-t:"))
c = float(input("Add meg c-t:"))

if (b**2 - 4 * a * c) < 0: # Ha a diszkrimináns negatív
    print("Az egyenletnek nincs megoldása a valós számok halmazán.")
elif (b**2 - 4 * a * c) == 0: # Ha a diszkrimináns 0
    x_1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2*a)
    print("Megoldás:", x_1)
else:
    x_1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2*a)
    x_2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2*a)
    print("Megoldások:", x_1, "és", x_2)
