#!/bin/python3

grosz,zlotowka,banknot = 'moneta groszowa','moneta złotowa','banknot'

nominaly = {\
        0.01 : grosz,
        0.02 : grosz,
        0.05 : grosz,
        0.10 : grosz,
        0.20 : grosz,
        0.50 : grosz,
        1.00 : zlotowka,
        2.00 : zlotowka,
        5.00 : zlotowka,
        10.0 : banknot,
        20.0 : banknot,
        50.0 : banknot,
        100. : banknot,
        200. : banknot,
        500. : banknot}

def Waluta(nominal):
    if nominal in nominaly:
        print('Podany nominał',nominal,'to',nominaly[nominal])

    else:
        print('Brak podanego nominału',nominal,'!')

def main():
    Waluta(100)
    Waluta(121)

if __name__=="__main__":
    main()
