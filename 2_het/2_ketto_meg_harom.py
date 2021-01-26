#!/usr/bin/env python3

# Ha nem integerként adjuk meg a változókat, a python azokat alapértelmezetten string-ként kezeli, így összeadásnál össze fogja fűzni azokat.
egyik = int(input("Írj be valamit: "))
masik = int(input("Írj be még valamit: "))
# Ha már integerként kérjük be a változók értékét, az összeadás helyes, amennyiben pedig nem integert ad meg a felhasználó, a program hibát dob.
print(egyik + masik)
