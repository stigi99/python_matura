import matplotlib.pyplot as plt
import numpy as np
"""
Wn = liczebnosc wilkow
Zn = Liczebnosc zajecy
Zn+1 = Zn + aZn - bZnWn
Wn+1 = Wn +bZnWn -cWn

a - współczynnik przyrostu liczby zajęcy,
b - współczynnik umierania zajęcy na skutek polowań wilkow
c - współczynnik umierania wilków

"""
Z = 100  # populacja startowa zajecy
W = 30  # populacja startowa wilkow
a = 0.02
b = 0.0005
c = 0.05


def zad_1(Z, W, a, b, c):
    for i in range(5 * 12):
        nZ = Z + a * Z - b * Z * W
        nW = W + b * Z * W - c * W
        Z = nZ
        W = nW
    print("Populacja zajecy ", round(Z,2), "Populacja wiklów ", round(W,2) )

def zad_2(Z,W,a,b,c):
    k=1
    odpZ=0
    odpW=0
    while not (odpZ or odpW):
        nZ = Z + a*Z -b*Z*W
        nW = W + b*Z*W - c*W
        if nZ<Z and not odpZ: odpZ = k
        if nW<W and not odpW: odpW = k
        Z = nZ
        W = nW
        k+=1
    print("Malejaca populacja zajecy ", odpZ, "Malejaca populacja wilkow", odpW)

def zad_3(Z,W,a,b,c):
    wilki = []
    zajece = []

    for i in range(20*12):
        nZ = Z + a*Z - b*Z*W
        nW = W + b*Z*W - c*W
        Z = nZ
        W = nW
        wilki.append(W)
        zajece.append(Z)
    miesience = range(0,20*12)
    plt.plot(miesience, wilki, color ='grey')
    plt.plot(miesience, zajece, color='brown')
    plt.xlabel('Kolejne miesiące')
    plt.ylabel("Liczebnosc populacji")
    plt.title("Populacja wilków i zajecy na przestrzeni 20 lat")
    plt.show()


def zad_4(Z,W,a,b,c):
    wilki =[]
    zajece = []
    for i in range(40*12):
        nZ = Z + a * Z - b * Z * W
        nW = W + b * Z * W - c * W
        Z = nZ
        W = nW
        wilki.append(round(W,2))
        zajece.append(round(Z,2))
    print("Minimalna populacja zajecy",min(zajece),"\n","Maksymalna populacja zajecy",max(zajece),'\n',
          "Minimalna populacja wilkow",min(wilki),'\n',"Maksymalna populacja wilkow",max(wilki))

numer=''
while True:
    print("Nacisnij q aby wyjsc")
    numer = input("Wpisz numer zadania\n")
    if numer == '1':
        zad_1(Z,W,a,b,c)
    elif numer =='2':
        zad_2(Z,W,a,b,c)
    elif numer =='3':
        zad_3(Z,W,a,b,c)
    elif numer =='4':
        zad_4(Z,W,a,b,c)
    elif numer =='q':
        break
    else:
        print("Nie cwaniakuj!")



