#!/bin/python3

## istnieje wbudowana funkcja round
#  ale nie poznaliśmy jej na zajęciach
#  zawsze można zapisać swoją własną

def Zaokraglenie(liczba,cyfraPoPrzecinku):
    ret = liczba * 10**cyfraPoPrzecinku
    kolejnaCyfra = ret-int(ret)
    ret = int(ret)  
    if kolejnaCyfra >= 0.5: ret+=1
    return ret * 10**(-cyfraPoPrzecinku)

# czas -- wyrazony w sekundach
def KonwersjaNaHMS(czas):
    
    sekundy = czas % 60
   
    # to polecenie jest opcjonalne nie będę od Państwa (narazie) wymagał
    sekundy = Zaokraglenie(sekundy,2)
    
    minuty = int(czas // 60)
    godziny = int(minuty // 60)

    print("czas [s]:", czas,"-->",end=' ')
    print(godziny,"h ",minuty,"m ",sekundy,"s ",sep='')

def main():
    KonwersjaNaHMS(234.45)

if __name__=="__main__":
    main()
