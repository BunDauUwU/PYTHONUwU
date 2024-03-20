w = int(input("Kich thuoc dia nho: "))
a = [int(i) for i in input("Kich thuoc cac dia: \n").split()]
a = sorted(a)
s = 0
cnt = 0
for i in a:
    s += i
    if(s > w):
        print(f"{cnt} dia nho")
        break
    cnt +=1
