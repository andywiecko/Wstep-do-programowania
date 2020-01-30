#!/bin/python3

########################################
# przykładowe rozwiązanie kolokwium
# plik zad1.py
########################################
# grupa B, zadanie 1
# Andrzej Więckowski
# Old Man Willow, 09-11-2019

def Mlynek(n):
    
    # wiersze
    for i in range(n):
        for j in range(n):
            print(abs(i-j)+1,' ',end='')

        # nowy wiersz
        print()

def main():
    Mlynek(10)

if __name__=="__main__":
    main()
