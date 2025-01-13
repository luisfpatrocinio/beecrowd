A, N = map(int, input().split())

while N <= 0:
    N = int(input())

sum = A
for i in range(1, N):
    sum += A + i

print(sum)