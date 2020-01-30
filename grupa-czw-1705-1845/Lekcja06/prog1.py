#!/bin/python3

def Trojkat(liczbaLinii):
    for nrLinii in range(liczbaLinii):
        liczbaGwiazdek = nrLinii + 1
        linia = liczbaGwiazdek * '*'
        print (linia)

def main():
    Trojkat(10)

if __name__=="__main__":
    main()

