#!/bin/python3

def IleDni(dzien1,dzien2):
    dniTygodnia = {\
            'poniedziałek' : 0,\
            'wtorek'       : 1,\
            'środa'        : 2,\
            'czwartek'     : 3,\
            'piątek'       : 4,\
            'sobota'       : 5,\
            'niedziela'    : 6}
    
    id1 = dniTygodnia[dzien1]
    id2 = dniTygodnia[dzien2]

    roznica = (id2 - id1) % 7
    return roznica

def main():
    print(IleDni('poniedziałek','niedziela'))
    print(IleDni('niedziela','poniedziałek'))

if __name__=='__main__':
    main()

