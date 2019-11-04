dane = open("tablica/dane.txt").read().splitlines()
dlugosc_tab=int(len(dane))
polowa = round(int(dlugosc_tab/2))
rosnaco = dane[:polowa]
malejco = dane[polowa:]
rosnaco = sorted(rosnaco)
malejco = sorted(malejco, reverse=1)
print(rosnaco)
print(malejco)