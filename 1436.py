arr = []
for i in range(int(1e+6)):
    if "666" in str(i):
        arr.append(i)
n = int(input())
print(arr[n-1])