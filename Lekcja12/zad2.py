#!/bin/python3

def Trojkat(h):
    wiersze = range(1,h+1)
    for wiersz in wiersze:
        kolumny = range(1,wiersz+1)
        for kolumna in kolumny:
            liczba = wiersz**kolumna
            print(f"{liczba:10d}",end=' ')
        print()
def main():
    Trojkat(10)    

if __name__=="__main__":
    main()
