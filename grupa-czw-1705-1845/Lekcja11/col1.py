#!/bin/python3

wiosna,lato,jesien,zima = 'wiosna','lato','jesień','zima'

poryRoku = { \
        'styczeń'     : zima,
        'luty'        : zima,
        'marzec'      : wiosna,
        'kwiecień'    : wiosna,
        'maj'         : wiosna,
        'czerwiec'    : lato,
        'lipiec'      : lato,
        'sierpień'    : lato,
        'wrzesień'    : jesien,
        'październik' : jesien,
        'listopad'    : jesien,
        'grudzień'    : zima}

def PoryRoku(miesiac):
    if type(miesiac) != type(str()):
        print('Błędny typ argumentu!')
        return 1

    if miesiac in poryRoku:
        print('Podany miesiąc',
                miesiac,
                'odpowiada następująca pora roku:',
                poryRoku[miesiac])

    else:
        print('Podano błędną nazwę miesiąca!')

def main():
    PoryRoku(5)
    PoryRoku('llalal')
    PoryRoku('grudzień')

if __name__=="__main__":
    main()
