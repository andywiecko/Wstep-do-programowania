#!/bin/python3

def SumaKwadratow(k,n):
    if not(type(k)==type(n)==type(int())):
        print ('Podano błędny argument funkcji!')
        return 

    suma = 0
    for i in range(k,n+1):
        suma += i**2
    return suma

def main():
    k = 0
    n = 10
    suma = SumaKwadratow(k,n)
    print('Suma kwadratów od',k,'do',n,'wynosi:',suma)

if __name__=='__main__':
    main()
