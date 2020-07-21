
"""
常见的算法排序
"""
"""
1.时间复杂度：
代码的执行时间T(n)等于每行代码的执行次数乘以每行代码的执行时间，所以用大O表示代码执行时间与代码执行次数成正比 T(n)=O(f(n))  f(n)为代码的最大执行次数
大O时间复杂度并不是表示代码真正的执行时间，而是代表执行时间随数据规模增长的变化趋势

2.算法稳定性：
相同元素在排序前后位置保持不变则称为稳定，稳定的排序算法如下：
冒泡排序是相邻的两个元素之间比较大小，相等的不会交换顺序
插入排序是在有顺序的子序列从后往前进行插入，相等的不会交换顺序
归并排序是分成一个个元素，然后再进行合并，再合并时相等的元素位置也不会交换
"""

#选择排序 前面元素依次和后面所有元素进行比较，选出最大或最小的放到前面，时间复杂度为O(n^2)
def choose_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    print(arr)

#冒泡排序 总共冒泡n-1轮，每轮是n-1-i个元素进行比较，时间复杂度为O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

#插入排序 是针对于有一定顺序的序列进行排序  时间复杂度 O(n^2)
def insert_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]  #表示要插入的值
        j = i-1  #要插入的值前面的元素序号
        while j >= 0:
            if arr[j] > value:  #从后往前遍历，如果找到比插入的数据大的，则该数字向后移动一位
                arr[j + 1] = arr[j]
            else:  #如果前面的元素比插入的值小直接退出循环
                break
            j -= 1
        arr[j + 1] = value
    print(arr)

#希尔排序，也叫增量排序，通过增量分组，对每组进行直接插入排序，最后增量为1的时候，整个文件被分为一组




