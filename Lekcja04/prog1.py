#a = ['ala', 232,43.654,'ma']
#
########################
#      PĘTLA FOR       #
########################
### [!] konstrukcja: for element in lista:
###     bezpośredno iterujemy po wszystkich elementach z listy
#for el in a:
#    if type(el)==type(''):
#        print(el)
#
### [!] 1. tworzymy listę liczb od 0 do n-1: range(n)
###     2. gdzie n to liczba elementów listy `a`: n = len(a)
###     3. odwołujemy się do elementów listy korzystając z konstrukcji `a[index]`,
###        gdzie `index` to liczba z zakresu 0 do len(a)-1
#for numEl in range(len(a)):
#    print(a[numEl])
#

########################
#     PĘTLA WHILE      #
########################
#a = 0
#
### [!] konstrukcja: while warunek:
###     polecenia z bloku while są wykonywane tak długo,
###     jak warunek podany na pętli jest spełniony (True)
#while a<20:
#    a += 1
#    print(a)
#
#suma=sum([1,2,3,45,7,85])
#print(suma)
#
# [!] zakresy list: lista[start:stop]
#print(a[-1])  # <-- ujemne indeksy: numerowanie od końca listy
#print(a[1:])
#print(a[:-1])
#print(a[1:4]

# Zadanie: program do sumowania listy
# input: lista
# output: suma z listy (float,int)
# [!] Uwaga - to jest bardzo naiwne rozwiązanie
#     takiego problemu. Dodawanie liczb zmiennoprzecinkowych
#     nie jest przemienne na komputerze: a+b != b+a
#     bardziej wyrafinowane funkcje sumujące powinny sortować liczby
#     przed ich dodaniem
def MojaSuma(lista):
    # w zmiennej `ret` przechowujemy sumę elementów
    ret = 0
    # "wyciągamy" wszystkie elementu po kolei z listy `lista`,
    # elementy są przechowywane w zmiennej `el`
    for el in lista:
        # powiększamy naszą sumę o wartość elementu `el`
        ret += el
    # wszystkie elementy zostały dodane -> zwracamy sumę `ret`
    return ret

# Zadanie: program wypisujący sumę n kolejnych liczb z ciągu Fibbonaciego
#          zaczynając od F_1.
#          Ciąg Fibbonaciego F_n jest zdefiniowany w następujący sposób:
#          F_1 = 0, F_2 = 1, ..., F_n = F_{n-1} + F_{n-2}
def Fibbonaci(n):
    # inicjalizujemy pierwsze dwa wyrazu ciągu: F_1, F_2
    ret = [0,1]
    # ukonujemy operację n-2 (brakuje n-2 elementów w `ret`)
    for i in range(n-2):
        # do listy `ret` dodajemy sumę dwóch ostatnich elementów
        ret.append(ret[-1]+ret[-2])  # <-- rozwiązanie iteracyjne, powiemy również o rozwiązaniu rekurencyjnym

    # program zwraca listę n liczb z ciągu Fibbonaciego
    # nie zwracamy bezpośrednio sumy jedynie w celu szybkiej weryfikacji
    # poprawności generowanego ciągu
    return ret
        

def main():
    # lista do przetestowania sumy
    a = range(100)
    
    # (naiwnie) sprawdzamy czy sumy są równe
    # [!] o ile lista zawiera typy int wszystko powinno działać
    #     w przypadku zmiennych float raczej nie dostaniemy tutaj True
    #     to zależy od liczb jakie będzie zawierać ta lista
    print (MojaSuma(a)==sum(a))

    # wyświetlamy n=10 pierwszych liczb z ciągu Fibbonaciego
    print (Fibbonaci(10))
    # wyświetlamy ich sumę
    print (sum(Fibbonaci(100)))

if __name__=='__main__':
    main()
