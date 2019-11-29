#!/bin/python3

########################################
# przykładowe rozwiązanie kolokwium
# plik zad1.py
########################################
# grupa B, zadanie 1
# Andrzej Więckowski
# Old Man Willow, 09-11-2019

def Rownanie(n):
    rozwiazania = []
    for x in range(n+1):
        for y in range(n+1):
            LHS = x**2+y**2
            RHS = 19*x+13*y
            if LHS == RHS:
                rozwiazania.append([x,y])

    return rozwiazania

def main():
    rozwiazania = Rownanie(100)
    liczbaRozwiazan = len(rozwiazania)

    print("Rozwiazania:",rozwiazania)
    print("Liczba rozwiazań:",liczbaRozwiazan)

if __name__=="__main__":
    main()
