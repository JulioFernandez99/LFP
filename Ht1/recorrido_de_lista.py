
lista=[11,12,13,14,15,16]

#Forma ascendente
print("-------Forma ascendete-------")
for dato in lista:
    print(dato)


#Forma descendente
print("\n-------Forma descendete-------")
size=len(lista)-1
for i in range(0,size+1):
     #print(f"{size}-{i}={size-i}")
     print(lista[size-i])