def min_operations(N, A, K):
    for x in A:
        if (x - A[0]) % K != 0:
            return -1
    B = [x // K for x in A]
    B.sort()
    median = B[N // 2]
    ops = sum(abs(x - median) for x in B)
    return ops

N = int(input())
A = list(map(int, input().split()))
K = int(input())
print(min_operations(N, A, K))