n = int(input())
for i in range(n):
    temp = input().split()
    itr, str = int(temp[0]), temp[1]
    for s in str:
        print(s*itr, end = '')
    print()