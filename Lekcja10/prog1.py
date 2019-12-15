#!/bin/python3

import math

def Silnia(n):
    if n < 1:
        return 1;
    else:
        ret = 1
        for i in range(1,n+1):
            ret *= i
        return ret

def SilniaRekurencyjnie(n): 
    if n < 1:
        return 1
    else:
        return n * SilniaRekurencyjnie(n-1)

def SilniaJednaLinijka(n): 
    return 1 if n < 1 else n * SilniaJednaLinijka(n-1)

def main():
    n = 40
    print('math.factorial:',math.factorial(n))
    print('Silnia:',Silnia(n))
    print('Silnia Rekurencyjnie:',SilniaRekurencyjnie(n))
    print('Silnia Jedna Linijka', SilniaJednaLinijka(n))

if __name__=="__main__":
    main()
