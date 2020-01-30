#!/bin/python3 

def IlePseudonimow():
    n = input("Podaj ile pseudonimów: ")
    try:
        return int(n)
    except:
        print("Błędny format!")
        return IlePseudonimow()

def Pseudonimy():
    pseudonimy = []
    n = IlePseudonimow()
    for i in range(n):
        pseudonim = input(f"Podaj pseudonim ({i+1}/{n}):")
        pseudonimy.append(pseudonim)
        
    pseudonimy.sort()
    print(pseudonimy)

def main():
    Pseudonimy()

if __name__=="__main__":
    main()
