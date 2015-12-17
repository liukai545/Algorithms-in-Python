# _*_ encoding:utf-8 _*_
# O(n^2)
import algorithm

list = [5, 5, 9, 7, 1, 0, 3, 6, 5, 11, 3]

for i in range(0, len(list)):
    for j in range(0, len(list) - i):
        if ((j + 1 < len(list))):
            if ((list[j] > list[j + 1])):
                algorithm.swap(list, j, j + 1)

print(list)
