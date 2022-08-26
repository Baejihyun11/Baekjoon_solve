#https://www.acmicpc.net/problem/1260
from collections import deque

#DFS 재귀로

def DFS(graph, v):
    if v in dfs_visited:
        return
    dfs_visited.append(v)
    print(v, end=" ")
    for node in sorted(graph[v]):
        DFS(graph, node)
    return

#BFS queue로
def BFS(graph, v):
    visited = []
    need_to_visit = deque()
    need_to_visit.append(v)
    while need_to_visit:
        cur = need_to_visit.popleft()
        if cur in visited:
            continue
        visited.append(cur)
        print(cur, end = " ")
        need_to_visit.extend(sorted(graph[cur]))
    return list()


N, M, v = map(int, input().split())
graph = dict()
for i in range(N):
    graph[i+1] = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_visited = []
DFS(graph, v)
print()
BFS(graph, v)