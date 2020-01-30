#!/bin/python
########################################
# przykładowe rozwiązanie kolokwium
# plik zad1.py
########################################
# grupa A, zadanie 1
# Andrzej Więckowski
# Old Man Willow, 09-11-2019

import math
Pole = lambda R: math.pi * R**2

def Kolo():
    R = float(input("Podaj promien kola R: "))
    print("Pole kola o promieniu R wynosi:", Pole(R))

def main():
    Kolo()

if __name__=="__main__":
    main()
