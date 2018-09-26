import time
#import array
def checkorder(lista):
	log = True
	nn=len(lista)//2
	for i in range(1,nn):
		if lista[i]>lista[i+1]:
			log = False; break
	return log

def shuffle(lista):
	nylista = list(lista)
	n=len(lista) #lenght of list
	nn = n//2
	for i in range(0,nn):
		nylista[i*2]=lista[i]
		nylista[n-i*2-1]=lista[n-i-1]
	return nylista

while True: #huvud prog | True funkar till avbrott
	n=int(input ('How many cards are there? The number should be even:  '))
	if n % 2 == 0: #rest från division 
		break
	else:
		continue
start_time = time.time()
numbers=list(range(0,n))
numbers=shuffle(numbers)
sh=1
while (checkorder(numbers) == False):
	sh+=1
	numbers=shuffle(numbers)
print ('It takes ',sh,'shuffles for ',n,'cards')
print("--- %s seconds ---" % (time.time() - start_time))
input('press enter')
