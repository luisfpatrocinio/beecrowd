# volume da esfera: 4/3 * pi * r³
r, l = list(map(int, input().split()))
volume = 4 / 3 * 3.1415 * r ** 3
print(int(l // volume))