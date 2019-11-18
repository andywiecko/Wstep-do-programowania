#!/bin/python3

def PierwszaGwiazdka(n):
    return ' '*(n+1)+'*'

def Srodek(i,n):
    return (n-i)*' '+'*'+i*' '+'*'+i*' '+'*'

def Linia(n):
    return (2*n+3)*'*'

def Romb(n):
    print(PierwszaGwiazdka(n))

    for i in range(n):
        print(Srodek(i,n))

    print (Linia(n))
    
    for i in range(n):
        print(Srodek(n-1-i,n))

    print(PierwszaGwiazdka(n))

def main():
    Romb(10)

if __name__=="__main__":
    main()
