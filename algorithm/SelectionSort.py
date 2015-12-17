# _*_ encoding:utf-8 _*_
import algorithm

list = [0, 8, 6, 4, 7, 1, 2, 5, 9, 6, 3, 1, 8, 7, 1, 6, 8, 7, 1, 3, 2, 4]

for i in range(0, len(list)):
    minidx = i
    for j in range(i, len(list)):
        if (list[j] < list[minidx]):
            minidx = j
    algorithm.swap(list, i, minidx)

print(list)
