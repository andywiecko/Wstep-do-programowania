#!/bin/python3

############################
# Słowniki
############################

# definicja slownika
slownik = {} # pusty slownik
slownik = {'pies' : 4} # słownik z jednym elementem
#            ^      ^
#            |      |
#          klucz   wartość
# dodawanie elementow do slownika

slownik['ala'] = 34
slownik['bartek'] = 36
slownik['kot'] = 4


# usuwanie elementow slownika
del slownik['pies']

# ważne metody słowników
print("Slownik:",slownik)
print("Klucze slownika:",slownik.keys()) 
print("Wartosci slownika:",slownik.values()) 

# slownik domyslnie iteruje po kluczach:
for klucz in slownik:
    print(klucz)

# Przykład zastosowania słowników
# rozwazmy funkcje wyznaczającą ocenę z kolokwium

def Ocena(liczbaPunktow):
    if liczbaPunktow > 50: 
        return 5
    elif liczbaPunktow > 40 and liczbaPunktow <= 50:
        return 4
    elif liczbaPunktow > 30 and liczbaPunktow <= 40:
        return 3
    else:
        return 2

# oraz jej wersje z wykorzystaniem slownika
def OcenaS(liczbaPunktow):
    oceny = {5 : [50,60],\
             4 : [40,50],\
             3 : [30,40],\
             2 : [ 0,30]}   # [!] uwaga wszystko moze być wartością w słowniku
                            #     ale nie każdy obiekt może być kluczem
                            #     (np. lista NIE może być kluczem!)

    for ocena in oceny:
        przedzial = oceny[ocena]
        dolnaGranica = przedzial[0]
        gornaGranica = przedzial[1]

        if liczbaPunktow > dolnaGranica\
                and liczbaPunktow <= gornaGranica:
            return ocena

liczbaPunktow = 32
print("Liczba zdobytych punktow:", liczbaPunktow, "Ocena:", Ocena(liczbaPunktow), "(Ocena test słownika)",OcenaS(liczbaPunktow))
print()

############################
# Formatowanie wyswietlania 
############################

# funkcja format
napis = 'Ala ma {} kota'

print(napis)
print(napis.format(1))
print(napis.format(1.323))
print()

napis = 'Ala ma {kot} kota i {pies} psy'
print(napis)
print(napis.format(kot=1,pies=34))
print(napis.format(pies=1,kot=1.323))
print()

napis = '{2} Ala ma {0} kota i {1} psy'
print(napis)
print(napis.format('pierwszy','drugi','trzeci'))
print()


napis = 'ala ma {kot:6.2f} kota'
#                    ^ ^^
#                    | ||__ typ danych do wyswietlenia
#                    | |___ liczba cyfr po przecinku
#                    |_____ szerokosc pola

import math
print(napis.format(kot=math.pi))
