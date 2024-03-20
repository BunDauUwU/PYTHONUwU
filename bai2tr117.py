inp = input().split()
n = int(inp[0])
m = int(inp[1])

# n = int(input("So vaccine yeu cau:"))
# m = int(input("Sp vaccine hien tai: "))
if(n <= m):
    print("0 ngay")
inp = input().split()
pa = int(inp[0])
pb = int(inp[1])

need = n - m
day = int(need / (pa + pb)) + (need % (pa+pb) != 0)
print(f"Can {day} ngay")