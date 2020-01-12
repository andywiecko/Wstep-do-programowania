
def IleOsobDoWczytania():
    n = input("Podaj liczbę osob do wczytania: ")
    try:
        return int(n)
    except:
        print("Błędny argument!")
        return IleOsobDoWczytania()

def DodajOsobe(osoby,n):
    it = len(osoby)+1
    imie = input(f"Podaj imię ({it}/{n}):")
    imie = imie.split()
    nazwisko = input(f"Podaj nazwisko ({it}/{n}): ")
    nazwisko = nazwisko.split()
    osoba = {'imię':imie, 'nazwisko':nazwisko}
    osoby.append(osoba)

def WczytajOsoby(n):
    osoby = []
    while len(osoby) < n:
        DodajOsobe(osoby,n)
    return osoby

def ZwrocDuze(napisy):
    ret = ''
    for napis in napisy:
        if len(napis) > 0:
            ret += napis[0].upper()
    return ret

def DodajInicjaly(osoba):
    imie = osoba['imię']
    nazwisko = osoba['nazwisko']
    inicjal = ZwrocDuze(imie) + ZwrocDuze(nazwisko)
    osoba['inicjal'] = inicjal

def StworzInicjaly(osoby):
    for osoba in osoby:
        DodajInicjaly(osoba)

def WyswietlOsoby(osoby):
    for osoba in osoby:
        print(' '.join(osoba['imię']),' '.join(osoba['nazwisko']),osoba['inicjal'])
        print('# [komentarz] liczba imion:',len(osoba['imię']))
        print('# [komentarz] liczba nazwisk:',len(osoba['nazwisko']))
              
def Inicjaly():
    n = IleOsobDoWczytania()
    osoby = WczytajOsoby(n)
    StworzInicjaly(osoby)
    WyswietlOsoby(osoby)

def main():
    Inicjaly()

if __name__=="__main__":
    main()
