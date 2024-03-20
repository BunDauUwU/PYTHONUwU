a = [int(i) for i in input().split()]
b = a.copy()
n = len(a)
for i in range (0,n,2):
	b[i] += 1
p = 0
q = 0
for i in range(n):
	if(a[i] & 1 == 0):
		p+=1;
	if(b[i] & 1 == 0):
		q+=1;
if(p < q):
	print("a it hon")
elif p == q:
	print("bang nhau")
else:
	print("b it hon")