h,m = map(int,input().split())
if m-45 < 0 :
    print((24+h-1)%24,end = " ")
    print(60+m-45, end = "")
else:
    print(f"{h} {m-45}")