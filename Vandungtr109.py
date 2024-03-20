a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
tong = 0
trungBinh = 0
for i in range(1, 13):
    a[i] = int(input(f"Tien dien thang {i}: "))
    tong += a[i]
trungBinh = tong/12
print(f"Tong tien dien la {tong}")
for i in range(1, 13):
    if(a[i] > trungBinh):
        print(f"Tien dien thang {i} la {a[i]} nhieu hon trung binh")