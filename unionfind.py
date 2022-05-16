H,W = map(int,input().split())
Q = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

color = [[0]*(W+5) for i in range(H+5)]

uf = UnionFind(H*W)

for i in range(Q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        x,y = a[1],a[2]
        x -= 1
        y -= 1
        color[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=H or ny < 0 or ny >= W:continue
            if color[nx][ny] == 1:
                uf.unite((x,y),(nx,ny))
    else:
        x1,y1,x2,y2 = a[1],a[2],a[3],a[4]
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        if color[x1][y1] == 1 and color[x2][y2] == 1 and uf.same((x1,y1),(x2,y2)):
            print("Yes")
        else:
            print("No")