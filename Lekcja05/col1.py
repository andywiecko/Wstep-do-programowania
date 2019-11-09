#!/bin/python
########################################
# przykładowe rozwiązanie kolokwium
# plik zad1.py
########################################
# grupa A, zadanie 1
# Andrzej Więckowski
# Old Man Willow, 09-11-2019

Pole = lambda a,b,c: 2*(a*b+a*c+b*c)

def Prostopadloscian():
    a = float(input("Podaj a = "))
    b = float(input("Podaj b = "))
    c = float(input("Podaj c = "))
    pole = Pole(a,b,c)
    if (a==b==c) : print("To jest sześcian!") # zadanie uznawane bylo rowniez bez sprawdzania czy a>0, b>0,c>0
    print("Pole prostopadloscianu:", pole)

def main():
    Prostopadloscian()

if __name__=="__main__":
    main()
