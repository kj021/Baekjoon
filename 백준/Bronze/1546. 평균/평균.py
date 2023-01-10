subject = int(input())
scores = list(map(int, input().split()))
mean = max(scores)

for i in range(subject):
    scores[i] = scores[i]/mean*100

print(sum(scores)/subject)