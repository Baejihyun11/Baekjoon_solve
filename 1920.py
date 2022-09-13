N = int(input())
N_arr = input().split(" ")
N_arr = [int(x) for x in N_arr]
M = int(input())
M_arr = input().split(" ")
M_arr = [int(x) for x in M_arr]
N_arr.sort()
for m in M_arr:
    start = 0
    end = N - 1
    ans = 0
    while start<=end:
        mid = (start + end) // 2
        if N_arr[mid] == m:
            ans = 1
            break
        elif N_arr[mid] < m:
            start = mid + 1
        else:
            end = mid - 1
    print(ans)