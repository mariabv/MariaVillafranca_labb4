import time
def br_search(v, target):
    """Returns True if the sorted list v contains target and False otherwise.
    Undefined behaviour if v is not sorted"""
    return helper(v, 0, len(v), target)

def helper(v, start, end, target):
    if start > end or start >= len(v):
        return False
    mid = (start+end) // 2
    if v[mid] == target:
        return True
    if v[mid] < target:
        return helper(v, mid+1, end, target)
    else:
        return helper(v, start, mid-1, target)
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
def linsokkup(lista,n):
	for i in range(len(lista)):
		ord = list(lista[i])
		nyord = ord[2]+ord[3]+ord[4]+ord[0]+ord[1]
		nylista = []
		for j in range (i+1,len(lista)):
			nylista.append(lista[j])
		if n == 1:
			log = linsok(nylista,nyord)
		elif n == 2:
			log = binsok(nylista,nyord)
		elif n == 3:
			log = br_search(nylista,nyord)
		else:
			log = False
		if log:
			print (lista[i],' -- ',nyord)
inpf  = open('ordlista.txt', 'r') #huvudprog start
record = inpf.readlines()
for i in range(len(record)):
	ord = record[i].split('\n')
	record[i]=ord[0]
n=int(input ('For linear search press 1, for binary search press 2,\nfor binary recoursive search press 3:  ')) #int gör om symboler till heltal
start_time = time.time()
linsokkup(record,n) #huvud-call
print("--- %s seconds ---" % (time.time() - start_time))
input('press enter')
