x,y,w,h = map(int,input().split())
arr = []
arr.append(abs(w-x))
arr.append(abs(0-x))
arr.append(abs(0-y))
arr.append(abs(h-y))
print(min(arr))