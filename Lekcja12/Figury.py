import Kolo
import Prostokat

def main():
    r = float(input("podaj promień"))
    
    pole = Kolo.pole(r)
    obwod = Kolo.obwod(r)
    print("Pole -- figura",Kolo.nazwa,'--',pole)
    print("Obwod -- figura",Kolo.nazwa,'--',obwod)
    
    a = float(input("podaj bok a"))
    b = float(input("podaj bok b"))
    
    pole = Prostokat.pole(a,b)
    obwod = Prostokat.obwod(a,b)
    print("Pole -- figura",Prostokat.nazwa,'--',pole)
    print("Obwod -- figura",Prostokat.nazwa,'--',obwod)

if __name__=="__main__":
    main()
