#!/bin/python3

A = lambda P,r,n,t: P*(1+r/n)**(n*t)

def Lokata(P,r,n,t):
    print("Kapitał początkowy:",P)
    print("Roczna stopa oprocentowania:", r*100,"%")
    print("Liczba kapitalizacji odsetek w roku:",n)
    print("Czas trwania lokaty [lata]:",t)
    print("Wartość lokaty wynosi:", A(P,r,n,t))

def main():
    P = 1000
    r = 0.24
    n = 4
    t = 4
    Lokata(P,r,n,t)

if __name__=="__main__":
    main()
