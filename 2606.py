#https://www.acmicpc.net/problem/2606

def BFS(graph):
    visited = []
    need_visit = [1]
    cnt = 0
    while need_visit:
        cur = need_visit.pop(0)
        if cur in visited:
            continue
        visited.append(cur)
        cnt += 1
        need_visit.extend(graph[cur])
    return cnt
        
        

cnt_node = int(input())
cnt_edge = int(input())
graph = dict()
for i in range(cnt_node):
    graph[i+1] = []

for i in range(cnt_edge):
    n,m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)
ans = BFS(graph)
print(ans-1)
