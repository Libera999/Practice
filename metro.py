N = 8
A = 6
B = 1

dist = abs(A-B) - 1

if dist < (N - dist - 2):
    print(dist)
else:
    dist_min = N - dist - 2
    print(dist_min)

list = [8, 1, 3, 2, 0]

print(sorted(list))
