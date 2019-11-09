#!/bin/python
########################################
# przykładowe rozwiązanie kolokwium
# plik zad2.py
########################################
# grupa A, zadanie 2
# Andrzej Więckowski
# Old Man Willow, 09-11-2019

def Wyrazy(napis):
    return len(napis.split())

def main():
    napis = input("Podaj jakiś napis: ")
    print("Podano",Wyrazy(napis),"wyraz(y)/(ów)")

if __name__=="__main__":
    main()
