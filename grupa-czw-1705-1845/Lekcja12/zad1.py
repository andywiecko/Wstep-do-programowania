#!/bin/python3

def Podzielne3(start,stop):
    ret = []
    for i in range(start,stop+1):
        if i % 3 == 0:
           ret.append(i)
    return ret

def main():
    wynik = Podzielne3(1,20)
    print(wynik)

if __name__=="__main__":
    main()
