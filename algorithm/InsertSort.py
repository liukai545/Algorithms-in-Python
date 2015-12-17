# _*_ encoding:utf-8 _*_
import algorithm

list = [1, 4, 9, 13, 34, 26, 10, 7, 4]

for i in range(0, len(list)):
    for j in range(0, i + 1)[::-1]:
        if (j - 1 >= 0):
            while (list[j] < list[j - 1]):
                algorithm.swap(list, j, j - 1)
    print list

print(list)


