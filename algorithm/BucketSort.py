# _*_ encoding:utf-8 _*_

# 1,桶排序是稳定的
# 2,桶排序是常见排序里最快的一种,比快排还要快…大多数情况下
# 3,桶排序非常快,但是同时也非常耗空间,基本上是最耗空间的一种排序算法


# 要求全是10以内的数字
list = [0, 8, 6, 4, 7, 1, 2, 5, 9, 6, 3, 1, 8, 7, 1, 6, 8, 7, 1, 3, 2, 4]

bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in list:
    bucket[i] += 1
print(bucket)
result = []
for i in range(0, 10):
    while bucket[i] != 0:
        bucket[i] -= 1
        result.append(i)
print(result)
