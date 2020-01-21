#1

with open("anagram.txt","r") as dane:
    linia = dane.read().splitlines()
    for wiersz in linia:
        wiersz = wiersz.split(" ")
        dlugosc = list(map(len, wiersz))
        print(dlugosc)
        if dlugosc.count(dlugosc[0]) == len(dlugosc):
            wiersz.append("\n")
            with open("odp_4a.txt","a") as zapis:
                zapis.write(' '.join(wiersz))


#2
with open("anagram.txt", "r") as dane:
    linia = dane.read().splitlines()
    for wyraz in linia:
        wyraz = wyraz.split(" ")
        if len(wyraz[0]) == len(wyraz[1]) == len(wyraz[2]) == len(wyraz[3]) == len(wyraz[4]):
            if set(wyraz[0]) == set(wyraz[1]) == set(wyraz[2]) == set(wyraz[3]) == set(wyraz[4]):
                print(wyraz)
