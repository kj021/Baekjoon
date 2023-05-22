from itertools import combinations
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    s = list(combinations(s, 6))
    for i in s:
        for j in i:
            print(j, end=' ')
        print()
    print()