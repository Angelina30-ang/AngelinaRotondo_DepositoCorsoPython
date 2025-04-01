#SEQUENZA DI FIBONACCI  fino a N
#stampare la sequenza di Fibonacci fino a N
#il programma dovrebbe stampare tutti i numeri della sequenza di Fibonacci
#minori o uguali a N

#somma dei due numeri precedenti per ottenere il successivo
#Fn = Fn-1 + Fn-2  -->  Fn-1 e Fn-2 sono i due valori precenti
#F0=0 e F1=1

#funzione che esegue la sequenza di Fibonacci
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        sequenza= Fibonacci(n-1) + Fibonacci(n-2)
    return sequenza
    
#l'utente inserisce il valore    
N_fib_utente=int(input("inserire un numero N > 1: "))

#ciclo per stampare tutti i numeri della sequenza 
#fino al valore inserito dall'utente
i=1
while i < N_fib_utente:
    
    risultato=Fibonacci(i)
    print(risultato)
    i+=1

