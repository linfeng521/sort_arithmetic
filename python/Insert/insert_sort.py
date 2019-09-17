'''
从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
将新元素插入到该位置后；后面元素需要移位
重复步骤2~5。
'''


def insert_sort(lst):
    n = len(lst)
    if n < 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1
            lst[j] = target
    return lst


li = [4, 3, 1, 5, 8, 9]
print(insert_sort(li))
