#!/bin/python3

def CzyObramowanie(i,j):
    if i==0 or j==0:
        if i==j:
            print('x',' ',end='')
        elif i!=0:
            print(i,' ',end='')
        else:
            print(j,' ',end='')
    else:
        print(i*j,' ',end='')

def TabliczkaMnozenia(n):
    for i in range(n+1):
        for j in range(n+1):
            CzyObramowanie(i,j)
        print()

def main():
    TabliczkaMnozenia(10)

if __name__=="__main__":
    main()
