#!/usr/bin/env python3

lista = [9, 5, 8, 2, 7, 5, 3, 8, 2, 1]
 
for x in range(0, len(lista)-1):
    for y in range(x + 1, len(lista)):
        if lista[x] > lista[y]:
            tmp = lista[x]
            lista[x] = lista[y]
            lista[y] = tmp
 
print(lista)

"""
A fenti algoritmus először y-hoz rendelve a lista indexeit, végig iterál azon,
és összehasonlítja az y-nadik indexű elemeket először a 0. (x) elemmel.
Ha az x-szedik nagyobb, az y-nadikkal kicseréli azt.
Ha y-nal végig ért, folytatja x=1, y=2-vel.

1. Helyes, mert végigmegyünk a listán,
és a lista fennmaradó részében mindig az éppen talált legkisebb elemet fogjuk
az x-edikre cserélni, és ezt végrehajtjuk a lista minden elemén.

2. O(n^2)-es, szóval nem gyors.

3. Nem annyira átgondolt, mire a külső ciklus újra lefut,
a belső csak 1 elemet pakolt jó helyre,
annak ellenére hogy végigment az egész tömbön.
A külső csak annyit "használ fel", hogy az x-edik elemig már rendezett lesz
a lista mire a következő x-hez érünk, azt a részt már nem kell újra vizsgálni.

4. A fölösleges cseréket kiküszöbölhetnénk, pl egy minhely változóval,
ami először kezdésnek x értékét veszi fel az y cikluson belül,
majd ha lista[minhely] > lista[y], y-t fogja megkapni.
Így a csere a külső ciklusban történhetne,
ami minden x iterációnál 1 elemet mozgatna, kizárólag a jó helyre,
(csere lista[minhely]-et lista[x]-szel), bár így sem sok lépést spórolunk meg.

5. A módszer ismerős, de a nevét nem tudom felidézni :|
