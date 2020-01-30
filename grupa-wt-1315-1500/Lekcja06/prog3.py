#!/bin/python3

def Binomial(n):
    ret = []
    ret.append([1])
    ret.append([1,1])

    for _ in range(n-2):
        nowyWiersz = []
        poprzedniWiersz = ret[-1]
        for i in range(len(poprzedniWiersz)-1):
            nowyWiersz.append(poprzedniWiersz[i]+poprzedniWiersz[i+1])
        nowyWiersz = [1] + nowyWiersz + [1]

        ret.append(nowyWiersz)

    return ret

# funkcji do wyswietlania od Panstwa nie bede wymagal :)
def Wyswietl(binomial):

    n = len(binomial)
    n_max = n//2
    maxLiczbaCyfr = len(str(binomial[-1][n_max]))

    for line in binomial:
        strline = [ str(s) for s in line]
        strline2=[]
        for s in strline:
            while len(s)<maxLiczbaCyfr: s=' '+s
            strline2.append(s)
        
        print((n-1)*maxLiczbaCyfr*" "+(maxLiczbaCyfr*" ").join(strline2))
        n-=1



def main():
    binomials = Binomial(10)
    print(binomials)
    
    Wyswietl(binomials)

if __name__=="__main__":
    main()
