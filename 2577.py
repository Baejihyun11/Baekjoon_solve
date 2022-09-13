arr = []
for i in range(3):
    arr.append(int(input()))
mul = 1
for i in range(3):
    mul *= arr[i]
mul = list(str(mul))
for i in range(0,10):
    if i!= 9:
        print(mul.count(str(i)))
    else:
        print(mul.count(str(i)), end = "")