# _*_ encoding:utf-8 _*_

list = [0, 8, 6, 4, 7, 1, 2, 5, 9, 6, 3, 1, 8, 7, 1, 6, 8, 7, 1, 3, 2, 4]


def merge(list1, list2):
    list = []

    # while list1 and list2:
    #     if list1[0] < list2[0]:
    #         list.append(list1.pop(0))
    #     if list1:
    #         if list1[0] >= list2[0]:
    #             list.append(list2.pop(0))

    while list1 and list2:
        list.append(list1.pop(0) if list1[0] <= list2[0] else list2.pop(0))

    while list1:
        list.append(list1.pop(0))
    while list2:
        list.append(list2.pop(0))
    print(list)
    return list


def mergeSort(list):
    length = len(list)
    if length <= 1:
        return list

    mid = length // 2
    left = mergeSort(list[0:mid])
    right = mergeSort(list[mid:])
    return merge(left, right)

l = mergeSort(list)

print(l)
