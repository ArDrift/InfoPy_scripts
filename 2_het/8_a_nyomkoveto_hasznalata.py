#!/usr/bin/env python3

a = 11220
b = 2002
while b > 0:
    temp = b
    b = a % b
    a = temp
 
print("lnko =", a)

# 1. A változó értéke a program végén 11.
# 2. A szorzat változó értéke ilyenkor 6720.
# 3. A b változó értéke ilyenkor 44.
