
kolor = 'zielony'
# `def` slowo kluczowe definicja funkcji, nawiasy: lista argumentow
def main():
    kolor = input("Jaki jest Twój ulubiony kolor?")
    return kolor

print("kolor="+kolor)
main()        # uwaga zmienna kolor nie jest okreslona jako globalna w funkcji main!
print("kolor="+kolor)

print()

print("kolor="+kolor)
kolor = main()    # do zmienej `kolor` przypisujemy obiekt ktory zwraca funkcja main
print("kolor="+kolor)

# problem mozemy rozwiazac inaczej, okreslajac, ze zmienna kolor to zmienna globalna
# słuzy do tego slowo kluczowe `global`
# (globalnych obiektow dobry programista unika za wszelka cenę 
#  dlaczego takie globalne obiekty nie sa bezpieczne, przekonaja sie Panstwo
#  na kursach w przyszlych semestrach)

kolor = 'zielony'
def main():
    global kolor
    kolor = input("Jaki jest Twój ulubiony kolor?")
    # [!] brak slowa `return` - funkcja nie musi cos zwracac (odpowiednik typu `void` z jezykow C/C++)

print("kolor="+kolor)
main()
print("kolor="+kolor)
