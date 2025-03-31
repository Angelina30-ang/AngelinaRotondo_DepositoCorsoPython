#esercizio2
#inserire due numeri che formano un intervallo
#i numeri sono interi


contatore=True
while contatore:
    num_1, num_2 = input("inserisci due numeri che definiscono un intervallo: ").split()
    num_1=int(num_1)
    num_2=int(num_2)
#due liste vuote di numeri pari e dispari da riempire
    num_pari=[]
    num_disp=[]
    #uso splat* per formare la lista di numeri a partire dagli estremi dell'intervallo dato
    numeri=[*range(num_1,num_2+1)]
    print(numeri)

    #separo i numeri della lista in due liste di valori: pari e dispari
    for num in numeri:
        if num%2==0:
            num_pari.append(num)
        else:
            num_disp.append(num)
    print("lista numeri pari: ", num_pari)
    print("lista numeri dispari: ",num_disp)

    rip=input("vuoi ripetere? y/n: ")
    if rip=="n":
        contatore=False
        break
    else:
        print("continua")