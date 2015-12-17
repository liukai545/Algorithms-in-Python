# _*_ encoding:utf-8 _*_
"""
大顶堆
"""


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0;

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_up(self, i):  # i应该是最后的插入的位置，向上调整堆的开始位置
        """
        percolate up 上过滤

        Args:
            i: 上虑开始的位置，一般为最后一个位置
        """
        while i // 2 > 0:
            if (self.heap_list[i] < self.heap_list[i // 2]):
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[i // 2]
                self.heap_list[i // 2] = temp
            i = i // 2

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2;
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1


a_list = [9, 6, 5, 2, 3]
heap = BinHeap()

heap.build_heap(a_list)
print(heap.heap_list)
print(heap.current_size)

heap.insert(10)
heap.insert(7)
heap.insert(5)

print(heap.heap_list)

while heap.current_size > 0:
    print(heap.del_min())
