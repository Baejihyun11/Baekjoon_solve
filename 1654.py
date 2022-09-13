import sys

input = sys.stdin.readline

N, K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
    
max_value = max(arr)

start = 1
end = max_value

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for a in arr:
        cnt+= a//mid
    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)