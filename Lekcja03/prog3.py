# zadanie
# FunkcjaKwadratowa(a,b,c):
#
# output:
#   - liczba rozwiązań (x\in R)
# szkic:
#  1. delta = b**2 - 4*a*c
#  2. sprawdź wartość delty
#  3.a delta<0 -> rozwiazania zespolone -> brak rozwiazań
#  3.b delta>0 -> 2 rozwiazania -> podaj rozwiazania
#  3.c delta=0 -> 1 rozwiazanie
#  3.d a=b=c=0 -> oo wiele rozwiazan

# funkcja lambda f
# zwraca wartosc wyrazenia: a*x**2+b*x+c
# uzycie: f(x,a,b,c)
f = lambda x,a,b,c: a*x**2+b*x+c

# funkcja wyswietla sprawdzana funkcje
def WyswietlFunkcje(a,b,c):
    print("Sprawdzana funkcja:")
    print(a,"x^2+",b,"x+",c,sep='')

# funkcja wyswietla warosc f(x0,a,b,c)
# gdzie x0 
def Sprawdzam(x,a,b,c):
    y = f(x,a,b,c)
    print("sprawdzenie:",y)
    if y==0.0: print("x0 to miejsce zerowe!")
    else: print("Upps... x0 to NIE jest miejsce zerowe!")

# funkcja sprawdza liczbę rozwiązań równania
# kwadratowego podanego przez użytkownika
def FunkcjaKwadratowa(a,b,c):
    WyswietlFunkcje(a,b,c)
    # sprawdzamy czy podane parametry odpowadają f(x)=0
    if a==b==c==0:
        print("oo wiele rozwiązań!")
    else:
        # obliczamy deltę
        delta = b**2 - 4 * a * c
        # pierwszy przypadek delta>0 -> 2 rozwiazania
        if delta>0:
            print("2 rozwiązania!")
            # liczymy rozwiązania ze wzoru
            x1 = (-b+delta**0.5) / (2*a)  # [!] Uwaga na nawiasy!
            x2 = (-b-delta**0.5) / (2*a)

            # wyswietlamy rozwiazania
            print("x1 =",x1)
            print("x2 =",x2)

            # sprawdzamy poprawnosc rozwiazań
            Sprawdzam(x1,a,b,c)
            Sprawdzam(x2,a,b,c)
            
        # drugi przypadek delta=0 -> 1 rozwiazanie
        elif delta==0:
            # obliczamy rozwiazanie ze wzoru
            x1 = -b / (2*a)

            # wyswietlamy rozwiazanie
            print("1 rozwiązanie!")
            print("x1 =",x1)

            # sprawdzamy rozwiazania
            Sprawdzam(x1,a,b,c)
        # delta < 0 brak rozwiazan rzeczywistych!
        else:
            print("brak rozwiązań!")

    # pusta linijka
    print()

def main():

    # testujemy: sprawdzamy czy wszystkie przypadki dzialaja
    FunkcjaKwadratowa(0,0,0)
    FunkcjaKwadratowa(1,-2,1)
    FunkcjaKwadratowa(1,-2,0)
    FunkcjaKwadratowa(1,0,1)

if __name__=="__main__":
    main()

