def bubble_sort(a):
    n = len(a)

    for i in range(0, n-1):
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


a = [22, 1, 12, 8, 3, 5]
print(bubble_sort(a))
