#!/bin/python3

def Header():
    print("[K]\t[°C]\t[°F]")
    print(30*'-')

def Fahrenheit(kelwiny):
    return 32+9./5.*Celsjusz(kelwiny)

def Celsjusz(kelwiny):
    return kelwiny - 273.15

def PodzialkaTermometru(T):
    print(T,Celsjusz(T),Fahrenheit(T),sep='\t')

def Termometr(start=0,stop=100,krok=10):
    Header()
    T = start
    while (T <= stop):
        PodzialkaTermometru(T)
        T += krok

def main():
    Termometr(0.0,140.5,15.5)

if __name__=="__main__":
    main()
