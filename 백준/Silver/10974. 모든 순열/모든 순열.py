from itertools import permutations
n= int(input())
for i in permutations([s for s in range(1,n+1)]):
    print(*i)