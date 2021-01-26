#!/usr/bin/env python3

print("1.", 1e200 / 1e-200)
# inf <- túlcsordulás miatt
print("2.", "igaz" if 1e3 + 1 == 1e3 else "hamis")
# hamis <- még elég kicsik a számok a pontos összehasonlításhoz
print("3.", "igaz" if 1e30 + 1 == 1e30 else "hamis")
# igaz <- 1*10^30 már túl nagy ahhoz hogy az "1"-es különbséget megkülönböztesse a program
