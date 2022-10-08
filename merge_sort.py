def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:

        if a[0] > b[0]:
            c.append(b[0])
            b.pop()
        else:
            c.append(a[0])
            a.pop()

    # a or b - empty
    while len(a) > 0:
        c.append(a[0])
        a.pop()

    while len(b) > 0:
        c.append(b[0])
        b.pop()

    return c


def sort_main(a):  # separate array to elements
    n = len(a)
    if n == 1:
        return a

    array1 = a[0:n//2-1]
    array2 = a[n//2:n]

    array1 = sort_main(array1)
    array2 = sort_main(array2)

    return merge(array1, array2)


array = [2, 12, 7, 8, 1, 16, 5, 31]
print(array[2:2])
# print(sort_main(array))
