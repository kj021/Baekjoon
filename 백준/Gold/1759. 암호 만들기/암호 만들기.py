from itertools import combinations
L, C = map(int,input().split())
alpha = sorted(input().split())
words = combinations(alpha, L) 
for word in words:
    cnt_vow = 0
    for i in word:
        if i in "aeiou":
            cnt_vow += 1
    if cnt_vow >=1 and L - cnt_vow >=2:
        print(''.join(word))