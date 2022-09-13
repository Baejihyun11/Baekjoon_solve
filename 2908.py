n,m = map(int,input().split())
n = list(str(n))
m = list(str(m))
n.reverse()
m.reverse()

n = int(''.join(n))
m = int(''.join(m))
if n>= m:
    print(n)
else:
    print(m)