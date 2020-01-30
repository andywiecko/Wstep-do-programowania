
def Dywanik(a,b):
    symbole = ['x','o','+']

    for i in range(a):
        for j in range(b):
            index = a*i+j
            jakiSymbol = index % len(symbole)
            print(symbole[jakiSymbol],end='')
        print()

def main():
    Dywanik(5,19)
    
    Dywanik(10,1)

if __name__=="__main__":
    main()
