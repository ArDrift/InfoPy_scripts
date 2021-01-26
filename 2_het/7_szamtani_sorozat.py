#!/usr/bin/env python3

print("Számtani sorozat")

diff = int(input("Add meg a differenciát:"))
hatar_1 = int(input("Add meg a sorozat alsó határát:"))
hatar_2 = int(input("Add meg a sorozat felső határát:"))

sorozat = []

if hatar_1 < hatar_2:
    min = hatar_1
    max = hatar_2
else:
    min = hatar_2
    max = hatar_1

if diff < 0:
    aktualis = max
    sorozat.append(max)
    while (aktualis + diff) > min:
        sorozat.append(aktualis + diff)
        aktualis = aktualis + diff

elif diff > 0:
    aktualis = min
    sorozat.append(min)
    while (aktualis + diff) < max:
        sorozat.append(aktualis + diff)
        aktualis = aktualis + diff
else:
    sorozat.append(min)
    print("A differencia 0, így a sorozat egyetlen eleme az alsó határa.")


print("A sorozat tagjai:", sorozat)
