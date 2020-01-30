#!/bin/python3

def Zapytanie():
    return int(input("Podaj liczbę ocen: "))

def PodawanieOcen(n):
    pass

def SredniaOcen(oceny):
    pass

def Wyswietlanie(oceny,sredniaOcen):
    pass

def SrednieOceny():
    n = Zapytanie()
    oceny = PodawanieOcen(n)
    sredniaOcen = SredniaOcen(oceny)
    Wyswietlanie(oceny,sredniaOcen)

def main():
    SrednieOceny()

if __name__=="__main__":
    main()
