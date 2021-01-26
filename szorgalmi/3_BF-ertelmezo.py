#!/usr/bin/env python3

import sys

adatszalag = [0] * 32768
programkod = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
fej_poz = 0
ciklus_melyseg = 0

cmd = 0

# utasítás-loop
while cmd in range(0, len(programkod)):
  # ha a fej a szalagon van
  if fej_poz in range(len(adatszalag)):
    # jobbra lép a szalagon
    if programkod[cmd] == ">":
      fej_poz += 1

    # balra lép a szalagon
    elif programkod[cmd] == "<":
      fej_poz -= 1
    
    # mutatott bájt növel
    elif programkod[cmd] == "+":
      adatszalag[fej_poz] += 1

    # mutatott bájt csökkent
    elif programkod[cmd] == "-":
      adatszalag[fej_poz] -= 1
    
    # mutatott bájt (karakter) kiírása
    elif programkod[cmd] == ".":
      sys.stdout.write(chr(adatszalag[fej_poz]))
    
    # karakter beolvasása bemenetről a mutatott bájtba
    elif programkod[cmd] == ",":
      # fájl vége jel
      adatszalag[fej_poz] = sys.stdin.read(1)
      if adatszalag[fej_poz] == "":
        adatszalag[fej_poz] == -1
        #print("A beolvasott byte üres.")
        break
      else:
        adatszalag[fej_poz] = ord(adatszalag[fej_poz])
    
    # ciklus kezdete
    elif programkod[cmd] == "[":
      # ha a ciklus lefut
      if adatszalag[fej_poz] > 0:
        ciklus_melyseg += 1
        ciklus_kezdet = cmd
      # ha nem fut le a ciklus
      else:
        while programkod[cmd] != "]":
          cmd += 1

        #cmd += 1
    
    # ciklus vége
    elif programkod[cmd] == "]" and ciklus_melyseg != 0:
      ciklus_melyseg -= 1
      cmd = ciklus_kezdet - 1
      
    cmd += 1
  else:
    print("A fej lelépett a szalagról, a program leáll.")
    break
  print(programkod[cmd - 1], fej_poz, adatszalag[fej_poz], ciklus_melyseg)
