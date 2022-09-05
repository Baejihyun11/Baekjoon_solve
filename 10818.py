n = int(input())
max = -1000000
min = 1000000
arr = input().split()
for i in range(n):
    t = int(arr[i])
    if max <= t:
        max = t
    if min >= t:
        min = t
print(f"{min} {max}")