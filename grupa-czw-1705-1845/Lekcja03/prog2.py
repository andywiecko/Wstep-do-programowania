
def fun(x):
    # slowo kluczowe `not`: 
    # operacja logiczna negacji: 
    # true -> false
    # false-> true
    # not (4>x) jest rownowazne zdaniu: 4 mniejsze/równe x
    if not (4>x):  
        print ("ok")
    # po dwukropku można napisać polecenie 
    # bez przejścia do nowej linii "\n"
    else: print ("not ok")
    print ("tutaj nie ma nowego bloku")

def main():
    fun(0)
    fun(5)

if __name__=="__main__":
    main()
 
