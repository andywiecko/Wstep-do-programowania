#!/bin/python3

def CelsjuszeNaFahrenheity(T):
    return 32 + 9./5. * T

def Header():
    return " Temperatura\n [C]\t [F]\n"+Linia()

def Linia():
    return 20*'='

def Termometr():
    zakresTemperatur = range(0,41,2)

    print(Header())
    
    for temperaturaC in zakresTemperatur:
        temperaturaF = CelsjuszeNaFahrenheity(temperaturaC)
        print(f"{temperaturaC:6.2f}\t{temperaturaF:6.2f}")

def main():
    Termometr()

if __name__=="__main__":
    main()
