#!/bin/python3

def Max(i,j):
    if i>j:
        return i
    else: 
        return j

    # mozna tez krocej
    # return i if i>j else j

def Ramka(n):
    for i in range(n+1):
        for j in range(n+1):
            # print(max(i,j),' ',end='') # [!] wbudowana funkcja max
            print(Max(i,j),' ',end='')   # [!] nasza własna implementacja
        print()

def main():
    Ramka(10)

if __name__=="__main__":
    main()
