ans_1 = []
ans_2 = []
temp1 = [0,1,0,1,0,1,0,1]
temp2 = [1,0,1,0,1,0,1,0]

def diff(arr1, arr2):
    sum = 0 
    for i in range(8):
        for j in range(8):
            if arr1[i][j]!= arr2[i][j]:
                sum += 1
    return sum

for i in range(8):
    if i%2 == 0:
        ans_1.append(temp1)
        ans_2.append(temp2)
    else:
        ans_1.append(temp2)
        ans_2.append(temp1)

n,m = map(int,input().split())
ori = []
for i in range(n):
    temp = input()
    t = []
    for j in temp:
        if j == "B":
            t.append(0)
        else:
            t.append(1)
    ori.append(t)

min = 64

for i in range(n-8+1):
    for j in range(m-8+1):
        a = diff([t[j:j+8] for t in ori[i:i+8]], ans_1)        
        b = diff([t[j:j+8] for t in ori[i:i+8]], ans_2)
        if a<= min:
            min = a
        if b<= min:
            min = b
print(min)
