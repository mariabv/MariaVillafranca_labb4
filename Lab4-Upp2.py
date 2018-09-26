def linsok(lista,elem):
	res = False
	for ord in lista:
		if ord == elem:
			res = True; break
	return res
inpf  = open('ordlista.txt', 'r')
record = inpf.readlines()
for i in range(len(record)):
	ord = record[i].split('\n')
	record[i]=ord[0]
while True:
	test=input('Ditt ord: ')
	if linsok(record,test):
		print (test+' finns'); continue
	else:
		print (test+' finns inte'); continue
input('press enter')
