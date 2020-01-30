#!/bin/python3

def DzialaniaNaLiczbach():
    a = int(input("Podaj a=..."))
    b = int(input("Podaj b=..."))

    print()
    print("Podstawowe działania dla a=",a," b=",b,":",sep='')
    print("Dodawanie: a+b=",a+b,sep='')
    print("Odejmowanie: a-b=",a-b,sep='')
    print("Mnożenie: a*b=",a*b,sep='')
    print("Dzielenie: a/b=",a/b,sep='')
    print("Dzielenie całkowite: a//b=",a//b,sep='')
    print("Dzielenie modulo: a%b=",a%b,sep='')
    print("Potęgowanie: a^b=",a**b,sep='')

def main():
    DzialaniaNaLiczbach()

if __name__=="__main__":
    main()
