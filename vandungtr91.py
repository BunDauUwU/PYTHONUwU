from math import *
a = float(input("Canh tam giac 1:"))
b = float(input("Canh tam giac 1:"))
c = float(input("Canh tam giac 1:"))
u = float(input("Canh tam giac 2:"))
v = float(input("Canh tam giac 2:"))
w = float(input("Canh tam giac 2:"))
p = float(input("Canh tam giac 3:"))
q = float(input("Canh tam giac 3:"))
r = float(input("Canh tam giac 3:"))
def S(a , b, c):
    return sqrt((a + b + c)*(a + b - c)*(a-b+c)*(b + c - a))/4
s1 = S(a, b, c)
s2 = S(u, v, w)
s3 = S(w, q, r)
print(f"Dien tich lon nhat {max(s1,max(s2,s3))}")
