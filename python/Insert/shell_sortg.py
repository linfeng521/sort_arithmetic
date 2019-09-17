'''
@author: me
@project: sortDemo
@file: shell_sortg.py
@time: 2019/9/18 0:45
@desc:
'''
def ShellSort(lst):
    def shellinsert(arr,d):
        n=len(arr)
        for i in range(d,n):
            j=i-d
            temp=arr[i]             #记录要出入的数
            while(j>=0 and arr[j]>temp):    #从后向前，找打比其小的数的位置
                arr[j+d]=arr[j]                 #向后挪动
                j-=d
            if j!=i-d:
                arr[j+d]=temp
    n=len(lst)
    if n<=1:
        return lst
    d=n//2
    while d>=1:
        shellinsert(lst,d)
        d=d//2
    return lst