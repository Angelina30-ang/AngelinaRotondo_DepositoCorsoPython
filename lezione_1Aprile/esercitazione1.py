#chiedere all'utente di inserire un numero intero positivo n

#ciclo while booleano per far ripetere l'inserimento del dato in caso di inserimento errato

contatore=True
while contatore:
    n=int(input("inserire un numero intero positivo: "))
    
    if n>0:
    #definiamo il range per prendere solo i numeri pari
        num_pari=[]
        for i in range(2,n+1,2):
            num_pari.append(i)
        print("numeri pari: ", num_pari)
        
        #somma dei numeri pari inseriti in una lista
        somma=sum(num_pari) 
        print("somma dei numeri pari: ", somma) 

        #definiamo i numeri dispari
        num_disp=[]
        for disp in range(1,n+1,2):
            num_disp.append(disp)
        print("numeri dispari: ", num_disp)

        #contatore False per uscire dal ciclo
        contatore=False
        break
    #se il numero inserito è <=0, ripete l'inserimento del numero    
    else:
        print("devi inserire un numero intero positivo")

#verificare se il numero n è primo
primo=True
if n<=1:
    primo =False
else:
    for i in range(2, int(n**0.5)+1):
        if n %i==0:
            primo=False
            break
        #non è un numero primo ed esce dal blocco

#condizione su primo se è vero è un numero primo, 
# altrimenti non è un numero primo       
if primo:
    print(n, " è un numero primo")
else:
    print(n, " non è un numero primo")