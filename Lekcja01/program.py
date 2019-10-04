
##############################
# PODSUMOWANIE ZAJEC 01
##############################
# podstawowe typy w pythonie
##############################
# definicje obiektow
# (uwaga! python ma mocne typowanie, 
#  ale nie ma deklaracji zmiennych
#  jak np. w jezyku c++)
#  
# int (integer) -- całkowite
a=2
b=4
c=-443
# float -- zmiennoprzecinkowe
a=2.4
b=45.0
c=-3354.3985
# str (string) -- ciag znakow
# napis = "Czerwony maluch"
#          ^^^           ^
#   index: 012           14
# napis[index] -- zwraca znak o danym indeksie
#                 o zakresach bedzie pozniej
a="Ala ma kota"
b="Kot ma Ale"
c="Jakis napis"
print(a[0])
print(len(a))       # len "liczy" dlugosc ciagu znakow
# list -- lista 
a=[]
b=['Ala',13,0.54]
c=['Ala ma kota',10]
print(len(c))       # len() "liczy" tez dlugosc list
# podstawowe dzialania
# +  dodawanie
# *  mnozenie
# /  dzielenie zmiennoprzecinkowe
# // dzielenie calkowite
# %  dzielenie modulo
# operacje na liczbach
print("2+4 =",2+4) # print wyswietlanie na ekranie
print("5/2 =",5/2)
print("5//2 =",5//2)
print("5%2 =",5%2)
# operacje na stringach
napis="Ala ma kota"
print(3*napis)     # mnożenie stringow
print(napis+"!!!") # laczenie stringow
# rzutowanie obiektow
print(float(5))       # konwersja na double
print(int(5.6))       # konwersja na int (!)
print("napis"+str(7)) # konwersja na string
# w pythonie wszystko jest obiektem!
# `obiekt`.`coś`            <- obiekt ma elementy
# `obiekt`.`coś(parametry)` <- obiekt ma funkcje
#                              wiecej o tym pozniej
# funkcja input -- wczytywanie ciagu znakow z klawiatury
wejscie = input("Podaj imie: ")
print("Twoje imie:", wejscie)
# wazne metody klasy string
# split() -- dzieli string i jako seperatora uzywa bialych znakow
#            (opcjonalny parametr mozna podac inny seperator! 
#             dowolny ciag znakow)
# join()  -- laczy stringi z listy
print("Ala ma kota".split())
print(" ".join(["wstep", "do", "programowania"]))
##############################
# zadanie 1
# napisz program ktory czyta z klawiatury imie i nazwisko
# i wyswietla je w formacie: `imie`_`nazwisko`
# rozwiazanie
imie=input("Podaj imie: ")
nazwisko=input("Podaj nazwisko: ")
login = imie+'_'+nazwisko
print(login)
##############################
# zadanie 2
# napisz program ktory czyta zdanie z klawiatury
# i wyswietla statystyki: liczbe wyrazow i liczbe znakow
# (bez bialych znakow)
# rozwiazanie
zdanie=input("Podaj zdanie: ")
wyrazy=zdanie.split()
litery="".join(wyrazy)
print("Liczba wyrazow:",len(wyrazy),"\nLiczba znakow:",len(litery))

# (nieobowiazkowe: funkcje lambda)
f = lambda x: x**2+2*x+1
g = lambda x: x**3+3
print (f(3))
print (g(3))
