n, x = map(int,input().split())
arr = input()
arr = arr.split(" ")
for a in arr:
    if int(a) < x:
        print(a, end = " ")