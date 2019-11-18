#!/bin/python3

def Choinka(liczbaLinii):
    for nrLinii in range(liczbaLinii):
        liczbaGwiazdek = 2*nrLinii + 1
        liczbaSpacji = liczbaLinii-1-nrLinii
        linia = liczbaSpacji * ' ' + liczbaGwiazdek * '*'
        print (linia)

    # pień
    pien = (liczbaLinii-1)*' '+'*' 
    for nrPnia in range(2): print (pien)

def main():
    Choinka(13)

if __name__=="__main__":
    main()

