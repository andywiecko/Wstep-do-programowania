
# zad2 z wykorzystaniem jednej pętli

def Trojkat(h):
    licznik = 1
    licznik2 = 1
    while licznik < h+1:
        
        print(licznik**licznik2,'',end='')
        
        if licznik2 < licznik:
            licznik2 += 1
        elif licznik2 == licznik:
            licznik2 = 1
            licznik += 1
            print()

def main():
    Trojkat(4)
    
if __name__=="__main__":
    main()
