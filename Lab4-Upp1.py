inpf  = open('ordlista.txt', 'r')
record = inpf.readlines()
for i in range(len(record)):
	ord = record[i].split('\n')
	record[i]=ord[0]
print (record[5])
print (len(record))
print (len(record[5]))
#new2
input('press enter')
