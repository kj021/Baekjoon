import sys
input = sys.stdin.readline
n = int(input())
perm = list(map(int, input().split()))
for i in range(n-1, 0, -1):
    if perm[i-1] < perm[i]:
        for j in range(n-1, 0, -1):
            if perm[i-1] < perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm = perm[:i] + sorted(perm[i:])
                print(" ".join(map(str, perm)))
                exit()
print(-1)