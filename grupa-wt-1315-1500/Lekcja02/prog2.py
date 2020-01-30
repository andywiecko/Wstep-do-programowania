
# [!] Dobry nawyk: nazwy funkcji zaczynac wielka litera: Funkcja()
def Imie():
    ret = input("Podaj imię:")  # [!] uwaga na wcięcia!
    return ret                  # kiedy interpreter napotka `return`,
                                # odrazu wychodzi z bloku funkcji 
                                # i zwraca obiekt znajdujacy się po nim 
    
def Kierunek():
    return input("Podaj kierunek:")

def Indeks():
    return input("Podaj nr indeksu:")

def main():

    # [!] Dobry nawyk: zmienne zaczynac mala litera
    imie = Imie()
    kierunek = Kierunek()
    indeks = Indeks()

    print(
    "\n"+                        
    "imię: "+imie,
    "kierunek: "+kierunek,
    "indeks: "+indeks,
    sep='\n',      # słowo kluczowe sep: oddziela stringi po przecinku podanym seperatorem
    end=''         # słowo kluczowe `end`: ostatni znak, standardowo jest to przejscie do nowej linii "\n"
    )

    print("\t #a gdzie nowa linia?")

main()
