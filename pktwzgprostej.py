print("Badanie położenia punktów A i B względem prostej y = ax+b")
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
print("")
print("Podaj współrzędne punktu A: ")
xa = float(input("xa: "))
ya = float(input("ya: "))
print("Podaj współrzędne punktu B: ")
xb = float(input("xb: "))
yb = float(input("yb: "))
ogolne1 = a*xa-ya+b
ogolne2 = a*xb-yb+b
wynik = ""
if ogolne1*ogolne2 < 0:
    wynik = "D"
elif ogolne1*ogolne2 > 0:
    wynik = "S"
elif (ogolne1 == 0 and ogolne2 != 0) or (ogolne2 == 0 and ogolne1 !=0):
    wynik = "J"
elif ogolne1 == 0 and ogolne2 == 0:
    wynik = "W"

print("Wynik: ",wynik)
