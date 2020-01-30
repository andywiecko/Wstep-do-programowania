# Wstęp do programowania
# Laboratorium 13 - zajęcia powtórzeniowe
# 13-17.01.2020
# imię:
# nazwisko:
# indeks:

# Zadanie 2 (15 pkt.)
# Napisz program, który oblicza wartości funkcji 1/x 
# dla argumentów z przedziału od -1 do 1.
# Liczba punktów powinna być podawana przez użytkownika z klawiatury.
# Jeśli użytkownik poda liczbę niedodatnia poproś o podanie
# liczby kolejny raz (aż do momentu uzyskania prawidłowej liczby).
# Wynik działania 1/x dla x = 0 zastąp slowem "NaN".
# Wyniki wypisz w postaci tabeli o dwóch kolumnach
# z liczbami zaokrąglonymi do 2 miejsc po przecinku.

# Przykładowy efekt działania programu.
#
# Podaj liczbe punktow: 11
# x		1/x
# -1.00 	 -1.00
# -0.80 	 -1.25
# -0.60 	 -1.67
# -0.40 	 -2.50
# -0.20 	 -5.00
# 0.00 		NaN
# 0.20 		 5.00
# 0.40 		 2.50
# 0.60 		 1.67
# 0.80 		 1.25
# 1.00 		 1.00

def WczytajLiczbe():
    liczba = input("Podaj liczbę punktów: ")
    try:
        liczba = int(liczba)
        if liczba >= 2:
            return liczba
        else:
            print("Podana liczba musi być większa od 2!")
            return WczytajLiczbe()
    except:
        print("Błędny format!")
        return WczytajLiczbe()

def PrzestrzenLiniowa(start,stop,n):
    ret = []
    x = start
    dx = (stop-start) / (n-1)
    for i in range(n):
        ret.append(x)
        x += dx
    return ret

def F(x):
    if abs(x) < 1e-10:
        return 'Nan'
    else:
       return 1./x

def Wyswietl(x,y):
    if type(y) == type(str()):    
        print(f"{x:6.2f}\t{y}")
    else:
        print(f"{x:6.2f}\t{y:6.2f}")

def Funkcja():
    liczbaPunktow = WczytajLiczbe()
    start = -1
    stop = 1
    for x in PrzestrzenLiniowa(start,stop,liczbaPunktow):
        Wyswietl(x,F(x))
        
def main():
    Funkcja()

if __name__=="__main__":
    main()
