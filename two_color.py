N = int(input())
edge = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
color = [0]*N
color[0] = 1
done = [0]*N
done[0] = 1

from collections import deque
que  = deque()
que.appendleft(0)
while que:
    p = que.popleft()
    for x in edge[p]:
        color[x] = (color[p]^1)
        if done[x] == 0:
            done[x] = 1
            que.appendleft(x)

res = []
cnt = color.count(1)
if cnt >= N//2:
    for i in range(N):
        if color[i]:
            if len(res) < N//2:
                res.append(i+1)
else:
    for i in range(N):
        if color[i] == 0:
            if len(res) < N//2:
                res.append(i+1)

print(*res)

import sys
sys.setrecursionlimit(10**8)
n = int(input())
edge = [[] for _ in range(n)]

for _ in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

color = [-1]*n

def dfs(pos, cur):
    color[pos] = cur
    for v in edge[pos]:
        if color[v] != -1:
            continue
        dfs(v, (cur^1))

dfs(0,0)
#print(color)
a1,a2 = [], []
for i in range(n):
    if color[i] == 0:
        a1.append(i+1)
    else:
        a2.append(i+1)
if len(a1) >= len(a2):
    print(*a1[:n//2])
else:
    print(*a2[:n//2])
