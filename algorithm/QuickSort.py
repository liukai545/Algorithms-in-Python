# _*_ encoding:utf-8 _*_

def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i - 1)
    quickSort(L, j + 1, high)
    return L


list = [5, 7, 3, 9, 22, 5, 3, 7, 8, 3, 634, 562, 123, 7, 346, 234,52,35, 1, 54,213, 54,213, 41, 523, 45, 4, 54, 5, 452, 5,
        21, 352, 345, 23, 45,234, 5, 52, 78,45, 87,46,8, 4]

l = quickSort(list, 0, len(list) - 1)

print(l)
