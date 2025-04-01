#programma che genera un numero casuale tra 1 e 100
#l'utente deve indovinare quale numero è stato generato
#deve dire all'utente se è minore o maggiore del numero generato
#il gioco finisce quando utente indovina o decide di uscire dal gioco

#modulo random per generare numeri random
import random

#funzione per il gioco
def gioco():
    random_num=random.randrange(1,101)

    #ciclo while per verificare se l'utente indovina o meno
    
    tentativo=True
    while tentativo:
        guess=int(input("indovina il numero: "))

        #se indovina il numero esce dal ciclo
        if guess==random_num:
            print("hai indovinato!")
            tentativo=False
            break
            
        #se numero è minore riprova o esce dal gioco 
        elif guess < random_num:
            print("il numero è troppo basso! Riprova")

            #scelta per l'utente se continuare o no il gioco
            #se decide di uscire la condizione diventa False ed esce dal ciclo
            
            scelta=input("vuoi continuare a giocare?y/n ")
            if scelta=="n":
                print("non hai indovinato. Il numero era: ", random_num)
                print("Fine gioco!")
                tentativo=False
                break
       
        #se il numero è troppo grande riprova o esce dal gioco
        else:
            print("il numero è troppo alto! Riprova")

            #se decide di uscire la condizione diventa False e esce dal gioco, altrimenti continua
            scelta=input("vuoi continuare a giocare?y/n ")
            if scelta=="n":
                print("non hai indovinato. Il numero era: ", random_num)
                print("Fine gioco")
                tentativo=False
                break
            
#chiamata del gioco            
gioco() 

    



