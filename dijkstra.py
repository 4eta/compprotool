n,m = map(int,input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    edge[a].append([b,1])
    edge[b].append([a,1])

from heapq import heappush, heappop
INF = 10 ** 10
mod = 1*10**9+7
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    num = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    num[s] = 1
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in edge[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False:
                if dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
                    num[to] = num[v]
                    num[to] %= mod
                    heappush(hq, (dist[to], to))
                elif dist[v] + cost == dist[to]:
                    num[to] += num[v]
                    num[to] %= mod
    return dist,num

D,cnt = dijkstra(1,n+1)

if cnt[n] == INF:
    print(0)
else:
    print(cnt[n])