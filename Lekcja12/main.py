
import kolo
import prostokat

def main():

    a,b = 4,5   
    nazwa = prostokat.nazwa
    print('Pole wybranej figury --',nazwa,'-- wynosi',prostokat.Pole(a,b))

    r = 5
    nazwa = kolo.nazwa
    pole = kolo.Pole(r)
    print('Pole wybranej figury --',nazwa,f'-- wynosi {pole:6.5f}',)


if __name__=="__main__":
    main()
