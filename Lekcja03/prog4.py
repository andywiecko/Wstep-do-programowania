# zadanie
# Sito(n)
# output: lista n pierwszych liczb pierwszych

# funkcja sprawdza, czy liczba `x` jest podzielna przez dowolna liczbę z listy `ret`
def SprawdzPierwszosc(x,ret):
    for i in ret:
        jestPodzielne = (x % i == 0)
        if jestPodzielne : return 0
    return 1  

# generuje listę `n` pierwszych liczb pierwszych
def Sito(n):
    ret = [] # zawiera liczby pierwsze
    x = 2    # liczba do sprawdzenia
    while len(ret)<n:
        czyPierwsza = SprawdzPierwszosc(x,ret)
        if czyPierwsza:
            ret.append(x) # dodaje `x` do `ret`, bo `x` jest pierwsza
        
        x += 1 # inkrementujemy `x`

    # blok petli `while` zakonczyl się: zwracamy listę liczb pierszych
    return ret

#SprawdzPierwszosc(6,[2,3,5])

myPrimes = Sito(10)
print(myPrimes)

# dodatkowe
# tym kodem proszę się nie przejmować
# sprawdzenie poprawności generowania liczb pierwszych
#import sympy
#primes = [sympy.prime(i+1) for i in range(10)]
#print(primes==myPrimes)
