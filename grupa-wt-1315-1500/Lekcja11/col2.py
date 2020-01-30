#!/bin/python3

def Wariacje(k,n):

    if (type(k) or type(n)) != type(int()):
        print('Podano błędny argument funkcji!')
        return 

    elif not (1 <= k <= n):
        return 0

    else:
        wariacje = n
        for i in range(n-k+1,n):
            wariacje *= i
        return wariacje

def main():
    n = 10
    k = 5
    wariacje = Wariacje(k,n)
    print(wariacje)

if __name__=="__main__":
    main()
