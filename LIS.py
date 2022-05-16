import bisect

def longest_Increasing_Subsequence(seq):
    LIS = [seq[0]]
    ret = []
    for i in range(len(seq)):
        cnt = bisect.bisect_left(LIS, seq[i])
        ret.append(cnt + 1)
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[cnt] = seq[i]

    return ret


N = int(input())
A = list(map(int, input().split()))

left = longest_Increasing_Subsequence(A)
right = longest_Increasing_Subsequence(list(reversed(A)))
right = list(reversed(right))

# get the len(LIS) :  max(longest_Increasing_Subsequence(A))

print(max(left[i]+right[i]-1 for i in range(N)))