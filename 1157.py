string = input()
string = string.upper()
arr = list(set(list(string)))
cnt = []
for s in arr:
    cnt.append(string.count(s))
if cnt.count(max(cnt))>= 2:
    print("?")
else:
    for idx, val in enumerate(cnt):
        if max(cnt) == val:
            print(arr[idx])
