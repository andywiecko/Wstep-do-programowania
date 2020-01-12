

def WczytajOsoby(n):
    osoby = []
    for i in range(n):
        imie = input("Podaj imię ({}/{}):".format(i+1,n))
        nazwisko = input("Podaj nazwisko ({}/{}):".format(i+1,n))
        osoba = {'imie' : imie,'nazwisko' : nazwisko}
        osoby.append(osoba)
    return osoby

def ZrobDuze(napis):
    if len(napis)>0:
        return napis[0].upper()
    else:
        return ''

def ZrobInicjal(osoba):
    imie = osoba['imie']
    nazwisko = osoba['nazwisko']
    imie_0 = ZrobDuze(imie)
    nazwisko_0 = ZrobDuze(nazwisko)
    return imie_0+nazwisko_0

def KonwertujDoInicjalow(osoby):
    inicjaly = []
    for osoba in osoby:
        inicjal = ZrobInicjal(osoba)
        osoba['inicjal'] = inicjal

def Wyswietl(osoby):
    for osoba in osoby:
        imie = osoba['imie']
        nazwisko = osoba['nazwisko']
        inicjal = osoba['inicjal']
        print("Imię:",imie,'| Nazwisko:',nazwisko,"| Inicjaly:",inicjal)

def Inicjaly():
    n = int(input("Podaj liczbę osób do wczytania"))
    osoby = WczytajOsoby(n)
    KonwertujDoInicjalow(osoby)
    Wyswietl(osoby)
