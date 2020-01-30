#####################################
# program: zmienne globalne
#####################################

# `kolor` to obiekt globalny
kolor = 'niebieski'

def UlubionyKolor():
    # slowo kluczowe `global`
    # informujemy że obiekt `kolor` to obiekt globalny
    # jesli nie uzyjemy slowa global
    # interpreter stworzy lokalny obiekt `kolor`
    global kolor 
    # mozemy wykorzystać operator przypisania
    # do zmiany obiektu globalnego
    kolor = input("Podaj swoj ulubiony kolor")

def main():
    print(kolor)    # wyswietli 'niebieski'
    UlubionyKolor() # nadpisujemy `kolor` za pomoca polecenia `input`
    print(kolor)    # wyswietli string z inputu

if __name__=="__main__":
    main()
