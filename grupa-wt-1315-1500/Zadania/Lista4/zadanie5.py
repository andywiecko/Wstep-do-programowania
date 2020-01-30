#!/bin/python3

stalaGrawitacji = 10.0

droga = lambda t: stalaGrawitacji*t**2/2.0

def SpadekSwobodny(czas):
    print ("Ciało po czasie [s]",czas,"przebyło drogę [m]",droga(czas))

def main():
    czas = float(input("Podaj czas spadania:..."))
    SpadekSwobodny(czas)

if __name__=="__main__":
    main()
