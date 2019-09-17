'''
依次比较相邻的元素,如果第一个比第二个大,则交换次序
对每一个相邻元素元素做同样的工作,从开始第一对到最后一对,这样最后一个就是最大的元素
针对所有的元素重复上述操作,除了最后一个
'''


def bubble_sort(lst):
    n = len(lst)
    if n < 1:
        return lst
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


li= [4, 3, 1, 5, 8, 9]
print(bubble_sort(li))
