arr = input().split()
num = 0
for i in arr:
    num += int(i)**2
print(num%10)