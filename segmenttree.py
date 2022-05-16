

w,n = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(n)]

INF = 10**12
W = 1*10**4+5
dp = [[-INF]*W for _ in range(n)]
for i in range(n):
    dp[i][0] = 0
#dp[i][j]:i番目まで見たときに重さjで達成できる最大の価値

def segfunc(x, y):
    return max(x,y)

ide_ele = -float("inf")

class SegmentTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

for i in range(A[0][0],A[0][1]+1):
    dp[0][i] = A[0][2]

seg = SegmentTree(dp[0], segfunc, ide_ele)

for i in range(1,n):
    for j in range(W):
        dp [i][j] = max(dp[i-1][j],seg.query(max(j-A[i][1],0),max(j-A[i][0]+1,0))+A[i][2])
    seg = SegmentTree(dp[i],segfunc, ide_ele)

print(max(dp[n-1][w],-1))

