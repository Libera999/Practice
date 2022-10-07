def bs(a, start, end, elem):
    if start <= end:
        middle = start+(end-start)//2
        if a[middle] == elem:
            return middle
        elif a[middle] < elem:
            return bs(a, middle+1, end, elem)
        else:
            return bs(a, start, middle-1, elem)
    else:
        return -1


array = [1, 5, 12, 34, 80, 120]
position = bs(array, 0, len(array)-1, 12)
print(position)
