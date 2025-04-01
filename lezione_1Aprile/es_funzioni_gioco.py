#programma che genera un numero casuale tra 1 e 100
#l'utente deve indovinare quale numero è stato generato

import random


def gioco():
    random_num=random.randrange(1,101)
    
    tentativo=True
    while tentativo:
        guess=int(input("indovina il numero: "))

        if guess==random_num:
            print("hai indovinato!")
            tentativo=False
            break

        elif guess < random_num:
            print("il numero è troppo basso! Riprova")
            scelta=input("vuoi continuare a giocare?y/n ")
            if scelta=="n":
                print("non hai indovinato. Il numero era: ", random_num)
                print("Fine gioco!")
                tentativo=False
                break

        else:
            print("il numero è troppo alto! Riprova")
            scelta=input("vuoi continuare a giocare?y/n ")
            if scelta=="n":
                print("non hai indovinato. Il numero era: ", random_num)
                print("Fine gioco")
                tentativo=False
                break
            
            
gioco() 

    



