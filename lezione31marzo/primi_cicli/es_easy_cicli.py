#PUNTO1:  if

num=int(input("inserisci un numero: "))

if num%2==0:
    print(num, " è un numero pari")
else:
    print(num, " è un numero dispari")



#PUNTO2: while e range

n=int(input("inserisci un numero intero positivo: "))

if n>=0:
  for i in range(n,-1,-1):
    print(i)
else:
   print("inserire numero positivo")

print()


while n>=0:
  print(n)
  n-=1
 
  
#PUNTO3: utilizzo di for
lista=[1,2,3,4,5]
quadrati=[]

#per ogni elemento della lista calcola il quadrato
#ogni quadrato viene inserito nella nuova lista 
for i in lista:
    quadrato=i**2
    quadrati.append(quadrato)
print(quadrati)

