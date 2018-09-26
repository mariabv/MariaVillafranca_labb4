import time
#Finns elementet x i den sorterade listan li ?
def binsok(li, x):
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
 #       print(li[mid])
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True
    return False
def linsok(lista,elem):
	res = False
	for ord in lista:
		if ord == elem:
			res = True; break
	return res
def linsokkup(lista):
	for i in range(len(lista)):
		ord = list(lista[i])
		nyord = ord[2]+ord[3]+ord[4]+ord[0]+ord[1]
		nylista = []
		for j in range (i+1,len(lista)):
			nylista.append(lista[j])
		if binsok(nylista,nyord):
			print (lista[i],' -- ',nyord)
start_time = time.time() #huvudprogrammet börjar här
inpf  = open('ordlista.txt', 'r')
record = inpf.readlines()
for i in range(len(record)):
	ord = record[i].split('\n')
	record[i]=ord[0]
linsokkup(record) #call börjar här
print("--- %s seconds ---" % (time.time() - start_time)) #snodde från internet, tiden det tar för programmet att köra 
input('press enter')
