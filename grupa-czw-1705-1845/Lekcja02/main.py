
# definicja funkcji, slowo kluczowe def
# w (...) podajemy listę argumentów
# na końcu po podaniu listy argumentów
# pamiętajmy o dwukropku `:`
def Kwadrat(a):  # `a` to jest argument funkcji Kwadrat()
    ret = a * a    # Uwaga na wcięcia!
    return ret   # `return` natychmiast 

def Trojkat(a,h):
    return 0.5 * a * h

def Prostokat(a,b):
    return a * b


def main():
    a = 5
    print("Pole kwadratu o boku a="+str(a),"wynosi P="+str(Kwadrat(a)))
    b = 2
    print("Pole prostokąta o boku a="+str(a),"oraz b="+str(b),"wynosi P="+str(Prostokat(a,b)))
    h = 4 
    print("Pole trojkata o boku a="+str(a),"oraz wysokosci h="+str(h),"wynosi P="+str(Trojkat(a,h)))

# dobry nawyk to umieszczanie w głównym skrypcie
if __name__=="__main__":
    main()
