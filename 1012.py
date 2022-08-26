#BFS
dxy = [(0,1),(0,-1),(1,0),(-1,0)]

def BFS(graph, x,y):
    need_visit = []
    need_visit.append((x,y))
    while need_visit:
        cur = need_visit.pop(0)
        if graph[cur[0]][cur[1]] == 0:
            continue
        graph[cur[0]][cur[1]] = 0
        for d in dxy:
            x_ = cur[0]+d[0]
            y_ = cur[1]+d[1]
            if x_>= N or x_ <= -1 or y_>=M or y_<= -1:
                continue
            if graph[x_][y_] == 1:
                need_visit.append((x_,y_))
    return True
            
T = int(input())
for t in range(T):
    N,M,K = map(int, input().split())
    farm = [[0]*M for i in range(N)]
    result = 0

    for k in range(K):
        i,j = map(int, input().split())
        farm[i][j] = 1
    
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                BFS(farm,i,j)
                result+=1
    print(result)
