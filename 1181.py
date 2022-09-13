n = int(input())
arr = []
for i in range(n):
    string = input()
    if string not in arr:
        arr.append(string)
arr.sort()
arr.sort(key = len)
for s in arr:
    print(s)