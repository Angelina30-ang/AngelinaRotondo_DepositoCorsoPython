#esercizio1
#numero o stringa e dire se pari o dispari
#se è una stringa deve contare le lettere della stringa


risposta=input("vuoi inserire un numero o una stringa? ")
contatore=True
while contatore:
    match risposta:

#se la risposta è un numero, lo rende intero e calcola se pari o dispari
        case "numero":
            num=int(input("inserisci il numero: "))
    
            if num%2==0:
                print("il numero è pari")
            else:
                print("il numero è dispari")
       
        case "stringa":
#se inserisce una stringa, calcola la lunghezza e dice se pari o dispari        

            stringa=input("inserisci la stringa: ")
            if len(stringa)%2==0:
                print("la stringa ha numero pari")
            else:
                print("la stringa ha numero dispari")
        
        case _:
            print("errore: Inserire un numero o una stringa")
    
    rip=input("Vuoi ripetere l'operazione? y/n")
    if rip=="n":
        controllore=False
        break
    else:
        print("continua")


