#Finns elementet x i den sorterade listan li ?
def binsok(li, x):
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        print(li[mid])
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True
    return False
def linsok(lista,elem): #behövs egenligen inte, appendix
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
	if binsok(record,test):
		print (test+' finns'); continue
	else:
		print (test+' finns inte'); continue
input('press enter')
