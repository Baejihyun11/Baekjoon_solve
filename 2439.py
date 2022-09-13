n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end ="")
    for k in range(i+1):
        if k != i:
            print("*", end = "")
        else:
            print("*")