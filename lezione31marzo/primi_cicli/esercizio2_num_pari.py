#ESERCIZIO 2: NUMERO INSERITO PARI

num=int(input("inserisci un numero: "))
pari=[]
if num%2 == 0:
    pari.append(num)
    print(num, " è un numero pari")
else:
    print("non è u numero pari")