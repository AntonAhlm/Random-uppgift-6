import random

tarning1=[1,2,3,4,5,6]
tarning2=[1,2,3,4,5,6]
lista=[]
a=int(input("Antal kast : "))
for i in range(0,a+1):
    tal1=random.choice(tarning1)
    tal2=random.choice(tarning1)
    print("Kast",i,":" , "Tal1 =",tal1,"   Tal2 = ",tal2,"   Summa = ",tal1+tal2) 
    lista.append(tal1+tal2)
print("\n")

for n in range (2,13):
    print("Antal med summa",n,":",lista.count(n))
