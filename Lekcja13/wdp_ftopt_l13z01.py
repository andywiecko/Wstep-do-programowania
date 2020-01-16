# Wstep do programowania
# Laboratorium 13 - zajęcia powtórzeniowe
# 13-17.01.2020
# imie:
# nazwisko:
# indeks:

# Zadanie 1 (15 pkt.)
# Napisz program, ktory:
# - pobiera od uzytkownika dlugosci trzech odcinkow,
# - sprawdza czy z tych odcinkow mozna zbudowac trojkat,
# - jesli tak to sprawdza czy jest to trojkat prostokatny,
# - jesli tak, to oblicza jego pole.
# W sytuacji, w ktorej jeden z warunkow nie jest spelniony
# program powinien wyswietlic odpowiednia informacje.

# Szczegolowe wymogi dotyczace implementacji programu:
# - pobierz od użytkownika zmienne odpowiedniego typu przechowujace
#   dlugosci odcinkow (2 pkt)
# - sprawdz czy podane odcinki w jakiejkolwiek konfiguracji
#   moga utworzyc trojkat (3 pkt)
# - jesli nie jest to mozliwe, wyswietl odpowiednia informacje
#   (1 pkt)
# - jesli jest to mozliwe, to sprawdz czy trojkat jest prostokatny
#   (3 pkt)
# - jesli jest to oblicz i wyswietl jego pole (4 pkt)
# - jesli nie jest, to wyswietl odpowiednia informacje (1 pkt)
# - zadbaj o to, aby program obliczal pole tylko dla trojkata
#   prostokatnego i nie powielal tych samych komunikatow w roznych
#   przypadkach (1 pkt)
# 
# Program bedzie oceniany tylko w przypadku,
# gdy bedzie mozna go uruchomic!
# ----------------------------------------------------
# Przykladowe wyniki uruchomienia programu:
# 
# Podaj dlugosci trzech odcinkow
# a: 3.0
# b: 4.0
# c: 5.0
# Trojkat jest prostokatny.
# Pole tego trojkata wynosi: 6.00
# ----------------------------------------------------
import math

def PobierzBok(nazwa):
    bok = input(f"Podaj {nazwa}: ")
    try:
        bok = float(bok)
        if bok > 0:
            return bok
        else:
            print("Bok musi być większy od 0!")
            return PobierzBok(nazwa)
    except:
        print("Błędny format!")
        return PobierzBok(nazwa)

def CzyTrojkat(a,b,c):
    boki = [a,b,c]
    boki.sort()
    a,b,c = boki    
    
    if a+b>c:
        return True
    else:
        return False

def CzyProstokatny(a,b,c):
    boki = [a,b,c]
    boki.sort()
    a,b,c = boki
    precyzja = 1e-16
    if abs(a**2+b**2-c**2)<precyzja:
        return True
    else:
        return False

def Pole(a,b,c):
    return 1./4.*math.sqrt(((a+b)**2-c**2)*(c**2-(a-b)**2))

def Trojkat():
    a = PobierzBok('a')
    b = PobierzBok('b')
    c = PobierzBok('c')

    if CzyTrojkat(a,b,c):
        print("To jest trójkąt!")

        if CzyProstokatny(a,b,c):
            print("Jest prostokątny!")

        pole = Pole(a,b,c)
        print(f"Pole trójkąt wynosi: {pole}")
        return pole
        
    else:
        print("To NIE jest trójkąt!")
        return 0

def main():
    Trojkat()

if __name__=="__main__":
    main()
    
