#esercizio_1

#scrivere programma che chiede all'utente la sua età
#se l'età è<18 , il programma stampa non puoi vedere questo film
#altrimenti puoi vederlo


age=int(input("inserisci la tua età: "))

if age<18:
    print("Mi dispiace, non puoi vedere questo film")
else:
    print("Puoi vedere questo film")


#esercizio_2
num_1, num_2 = input("inserisci due numeri: ").split()
num_1=int(num_1)
num_2=int(num_2)

operazione =input("inserisci operazione da eseguire tra '+', '-', '*', '/': ")

if operazione== "+":
    sum = num_1 + num_2
    print("somma: ", sum)
elif operazione=="-":
    sott=num_1-num_2
    print("sottrazione: ", sott)
elif operazione == "*":
    molt=num_1*num_2
    print("moltiplicazione: ", molt)
elif operazione == "/":
     if num_1==0 or num_2==0:
         print("Errore:divisione per zero")
     else:
        div=num_1/num_2
        print("divisione: ", div)
else:
    print("Operazione non riconosciuta")

