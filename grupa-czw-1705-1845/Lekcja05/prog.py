#!/bin/python

####################################
# definicje z przecinkiem
####################################
a,b,c = 1,2,3
print(a,b,c)

# funkcja zwracająca kilka elementów
def ZwrocDwaElementy(a,b):
    return a,b  # <-- ta funkcja zwraca tuple

# tuple -> niepodyfikowalna lista
tupla = (1,2,3)


####################################
# wszystko jest obiektem!
####################################
listaFunkcji = [print,ZwrocDwaElementy]
A = listaFunkcji[1]('ala','kot')
print(A)


####################################
# słowo komentarza o `in`
####################################
A = ['ala', 'ma', 'kota']

# możemy się zapytać, czy lista `A` 
# zawiera obiekt `'ala'`:
if 'ala' in A: print("'ala' jest w lista A!")

####################################
# import bibliotek
####################################
import math  # [!] odwolujemy sie poprzez nazwe modulu: `math`
print(math.pi,math.cos(0.5*math.pi))

#bardzo niebezpieczny import nadpisujacy ewentualne nasze definicje obieków!
from math import sqrt
print(sqrt(2))   # [!] przy takim imporcie zapominamy o nazwie modulu
# [!] nie zalecane!!!
from math import * # [!] import "wszystkiego" z modulu math

####################################
# [!] Ważne metody obiektów typu list
####################################
lista = ['ala','ma','kota']
print(lista)
print(lista.count('ala'))  # liczy wystapienia 'ala'
print(lista.index('ala'))  # zwraca index elementu 'ala'
lista.remove('ala')        # usuwa pierwszy element 'ala'
print(lista)
print(lista.pop(-1))       # usuwa oraz zwraca element o podanym indeksie
print(lista)

lista.insert(0,'a')       # wstawia element w podany indeks 
print(lista)

# sortowanie
lista = [1,2,324,45,12,57,2357]
print(lista)
lista.sort()               # sortowanie listy
print(lista)
lista.sort(reverse=True)
print(lista)

# sortowanie dziala na dowolne elemnty ktore mozna ze soba porownac
lista = ['ala', 'ma', 'kota', 'a', 'kot', 'ma', 'ala']
print(lista)
lista.sort()
print(lista)
