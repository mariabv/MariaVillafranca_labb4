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
		if linsok(nylista,nyord):
			print (lista[i],' -- ',nyord)
inpf  = open('ordlista.txt', 'r')
record = inpf.readlines()
for i in range(len(record)):
	ord = record[i].split('\n')
	record[i]=ord[0]
linsokkup(record)
input('press enter')
