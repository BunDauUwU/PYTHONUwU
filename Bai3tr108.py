# print("Nhap vao mot day so size giay")
# shoes = [int(s) for s in input().split()]
# sum = 0
# for i in range(len(shoes)):
# 	sum = sum + shoes(i)
# if(sum > 0):
# 	print("Giay ben trai, kich co", sum)
# else:
# 	print("Giay ben phai, kich co", sum)

print("Nhap vao mot day so size giay")
shoes = [int(s) for s in input().split()]
sum = 0
n = len(shoes)
shoes = sorted(shoes)
checker = 0
for i in range(len(shoes)):
	sum = sum + shoes[i]

if(sum > 0):
	print("Giay ben trai, kich co", sum)
else:
	print("Giay ben phai, kich co", -sum)
