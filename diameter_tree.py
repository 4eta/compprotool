# N: 木Tの頂点数
# edge[u] = [(w, c), ...]:
# 頂点uに隣接する頂点wとそれを繋ぐ辺の長さc
N = int(input())
edge = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    edge[a-1].append([b-1,1])
    edge[b-1].append([a-1,1])

from collections import deque
def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in edge[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    d = max(dist)
    return dist.index(d), d
u, _ = bfs(0)
v, d = bfs(u)
# パスu-vがこの木Tの直径(長さd)
# print(d)
print(d+1)
