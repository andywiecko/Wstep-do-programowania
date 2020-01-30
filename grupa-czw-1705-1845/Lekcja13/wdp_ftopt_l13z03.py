# Wstęp do programowania
# Laboratorium 13 - zajęcia powtórzeniowe
# 13-17.01.2020
# imię:
# nazwisko:
# indeks:

# Zadanie 3 (10 pkt.)
# Napisz program, który dla podanej przez użytkownika
# liczby rzeczywistej zwróci jej część ułamkową.
# W tym celu zdefiniuj funkcję czesc_ulamkowa,
# która zwraca część ułamkową liczby rzeczywistej
# podanej jako jej argument.
# Wywołanie funkcji czesc_ulamkowa() umieść w funkcji main(),
# rozważana liczba rzeczywista powinna zostać wprowadzona
# przez użytkownika z klawiatury.
# Wynik wyświetl w funkcji main() w stosownym formacie.

import math

def PobierzLiczbe():
    liczba = input("Podaj liczbę rzeczywistą (do 3 miejsc po przecinku): ")
    try:
        return float(liczba)
    except:
        print("Błędny format!")
        return PobierzLiczbe()

def CzescUlamkowa(liczba):
    czescUlamkowa = liczba - math.floor(liczba)
    return czescUlamkowa

def main():
    liczba = PobierzLiczbe()
    cz_ulamkowa = CzescUlamkowa(liczba)
    print(f"Podano liczbę: {liczba:6.3f}")
    print(f"Jej część ułamkowa wynosi: {cz_ulamkowa:6.3f}")

if __name__=="__main__":
    main()
