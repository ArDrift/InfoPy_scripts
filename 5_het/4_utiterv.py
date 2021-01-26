#!/usr/bin/env python3

def routeplan(dlist, dcount):

  speed = 100
  route = []
  
  for elem in dlist:
    route.append(str(elem) + " km, ")
  
  driven = 0

  for dist in range(0, len(dlist) - 1):
    driven += dlist[dist]
    # ha a következő úttal együtt az eddig vezetett út több másfél óránál
    if (driven + dlist[dist + 1]) / speed > 1.5:
      route.insert(dist + 1, "szünet." + "\n")
      driven = 0

  route.append("vége.")

  routestr = ""
  
  for elem in route:
    routestr += elem

  return routestr


def main():

  distcount = int(input("Add meg a távolságok számát: "))
  distlist = []

  for _ in range(distcount):
    distlist.append(float(input("Add meg a távolságot km-ben: ")))
    
  print(routeplan(distlist, distcount))
  
  return


main()
