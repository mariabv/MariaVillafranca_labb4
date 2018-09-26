def br_search(v, target): #basfall /kopieras
    """Returns True if the sorted list v contains target and False otherwise.
    Undefined behaviour if v is not sorted""" #sätt att kommentera
    return helper(v, 0, len(v), target)


def helper(v, start, end, target):#v=listan target=ordet vi söker / rekursivt anrop
    if start > end or start >= len(v):
        return False #utgång om vi inte fann ordet
    mid = (start+end) // 2
    if v[mid] == target:
        return True #utgången från programmet om vi fann ordet
    if v[mid] < target:
        return helper(v, mid+1, end, target) #kopieras inte
    else:
        return helper(v, start, mid-1, target)
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
	if br_search(record,test):
		print (test+' finns'); continue
	else:
		print (test+' finns inte'); continue
input('press enter')
