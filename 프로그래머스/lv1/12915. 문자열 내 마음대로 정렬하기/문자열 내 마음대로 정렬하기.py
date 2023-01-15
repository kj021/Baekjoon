def solution(strings, n):
    new = []
    for i in strings:
        new.append(i[n]+i)
    new.sort()
    answer= []
    for i in new:
        answer.append(i[1:])
    return answer