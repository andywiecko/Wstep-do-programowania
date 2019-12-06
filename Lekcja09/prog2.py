#!/bin/python3

import random

# sprawdzamy czy podany numer jest liczba calkowita
def CzyInt(numer):
    if type(numer) == type(int()): return True
    else: return False

# sprawdzamy czy podany numer jest w dziedzinie funkcji
def CzyDziedzina(numer):
    if numer in range(0,36+1): return True
    else: return False

def CzyParzyste(numer):
    if numer % 2 == 0: return True
    else: return False

def RuletkaIfy(numer):
    if not CzyInt(numer): return
    if not CzyDziedzina(numer): return

    kolor = None
    parzystosc = numer % 2

    if numer == 0:
        kolor = 'zielony'
    elif numer in range(1,10+1):
        if CzyParzyste(numer):
            kolor = 'czarny'
        else: 
            kolor = 'czerwony'
    elif numer in range(11,18+1):
        if CzyParzyste(numer):
            kolor = 'czerwony'
        else:
            kolor = 'czarny'
    elif numer in range(19,28+1):
        if CzyParzyste(numer):
            kolor = 'czarny'
        else:
            kolor = 'czerwony'
    elif numer in range(29,36+1):
        if CzyParzyste(numer):
            kolor = 'czerwony'
        else:
            kolor = 'czarny'


    print("Numer:",numer)
    print("Kolor:",kolor)

# ruletka na słownikach
def Ruletka(numer):
    if not CzyInt(numer): return
    if not CzyDziedzina(numer): return

    przedzialy = {\
            'A' : range(0,0+1),\
            'B' : range(1,10+1),\
            'C' : range(11,18+1),\
            'D' : range(19,28+1),\
            'E' : range(29,36+1)}

    kolory = {\
            'A' : ['zielony'],\
            'B' : ['czarny','czerwony'],\
            'C' : ['czerwony','czarny'],\
            'D' : ['czarny','czerwony'],\
            'E' : ['czerwony','czarny']}

    wylosowanyPrzedzial = None

    for przedzial in przedzialy:
        zakres = przedzialy[przedzial]
        if numer in zakres:
            wylosowanyPrzedzial = przedzial
            break
   
    parzystosc = numer % 2
    kolor = kolory[wylosowanyPrzedzial][parzystosc]

    print("Numer:",numer)
    print("Kolor:",kolor)



def main():
    # pseudo-losowa liczba całkowita z zakresu [0,36]
    numer = random.randint(0,36)
    RuletkaIfy(numer)
    Ruletka(numer)

if __name__=="__main__":
    main()
