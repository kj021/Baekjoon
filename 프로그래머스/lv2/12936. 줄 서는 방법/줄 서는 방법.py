import math
def solution(n,k):
    lst = [x for x in range(1, n+1)]
    answer = []
    k -= 1
    for i in range(n,0,-1):
        max_num = math.factorial(n)
        split_num = max_num //n
        answer.append(lst[k//split_num])
        lst.pop(k//split_num)
        k %= split_num
        n -=1
    return answer