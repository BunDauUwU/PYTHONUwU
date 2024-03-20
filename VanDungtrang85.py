n = int( input("So ga va cho:"))
m = int( input("So chan ga va cho:"))
for i in range(1, n):
    if(i*2 == (n-i)*4):
        print(f"So ga:{i}, so cho: {n-i}")
