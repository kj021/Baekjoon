import sys

T = int(input())

for i in range(0, T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)