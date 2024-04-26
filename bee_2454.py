p, r = list(map(int, input().split()))
result = -1
if p == 0:
    result = 2
else:
    if r == 0:
        result = 1
    else:
        result = 0
print(['A', 'B', 'C'][result])