def select_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst


li = [4, 3, 1, 5, 8, 9]
print(select_sort(li))
