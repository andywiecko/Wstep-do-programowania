#!/bin/python3

########################################
# przykładowe rozwiązanie kolokwium
# plik zad1.py
########################################
# grupa B, zadanie 1
# Andrzej Więckowski
# Old Man Willow, 09-11-2019

def Modulo(n):
    rozwiazania = []
    for x in range(n+1):
        for y in range(n+1):
            LHS = 2*x**2-y-5
            if LHS % 7 == 0:
                rozwiazania.append([x,y])

    return rozwiazania

def main():
    rozwiazania = Modulo(10)
    liczbaRozwiazan = len(rozwiazania)

    print("Rozwiazania:",rozwiazania)
    print("Liczba rozwiazań:",liczbaRozwiazan)

if __name__=="__main__":
    main()
