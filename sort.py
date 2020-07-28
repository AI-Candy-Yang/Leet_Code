
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

非线性时间比较类排序：通过比较来决定元素见的相对次序，由于其时间复杂度不能突破O(nlogn)，因此称为非线性比较类排序，
                        常见的插入，选择，归并都是

线性时间非比较类排序：不能通过比较来决定元素间的相对次序，可以突破基于比较排序的时间下界，以线性时间运行，
                        主要包括计数排序，桶排序，基数排序等   
                        
时间复杂度：
1.平方阶（n^2)  插入，选择，冒泡
2.线性对数阶（O(nlogn)) 快速，归并，堆
3.特殊的归并（O(n^(1.3-2))
4.线性  基数，桶，箱，计数等         
"""

#选择排序 前面元素依次和后面所有元素进行比较，选出最大或最小的放到前面，时间复杂度为O(n^2)
def choose_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    print(arr)

#冒泡排序 依次比较相邻的两个元素，将大的往后移，每轮会将最大的放到最后
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

#插入排序 是针对于有一定顺序的序列进行排序  时间复杂度 O(n^2)
def insert_sort(arr):
    for i in range(1,len(arr)):
        j,cur = i,arr[i]  #要插入的值和对应的下标
        while j > 0 and arr[j-1] > cur:  #比较这个插入的值和前面的值大小，比前面小的话，就将前面的值后移
            arr[j] = arr[j-1]  #将前面的值后移
            j -= 1  #将要插入的值的索引向前移动
        arr[j] = cur
    print(arr)

#希尔排序，也叫增量排序，通过增量分组，对每组进行直接插入排序，最后增量为1的时候，整个文件被分为一组
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap,len(arr)):
            j,cur = i,arr[i]  #要插入的值和下标
            while (j-gap) >= 0 and (arr[j-gap] > cur):
                arr[j] = arr[j-gap]
                j = j -gap
            arr[j] = cur
        gap = gap // 2

    print(arr)

#快速排序  挖坑---填数----分治  通过找基准值，然后不断的挖坑填数实现每一轮的排序
def quick_sort(arr,left,right):
    if left >= right:
        return arr
    pivot,i,j = arr[left],left,right
    while i < j:
        while i < j and arr[j] > pivot:
            j -= 1
        arr[i] = arr[j]  #从右向左找，找到比基准值小的，用这个值填基准值位置的坑

        while i < j and arr[i] < pivot:
            i += 1
        arr[j] = arr[i]  #从左往右找，找到比基准值大的，用这个值来填上个坑
    arr[j] = pivot  #最终i=j的时候退出循环，基准值填坑
    quick_sort(arr,left,j-1) #对基准值前的序列递归排序
    quick_sort(arr,j+1,right) #对基准值后的序列递归排序
    print(arr)

#归并排序 采用分治思想，先将数列递归分成一个个元素，然后从下至上的合并

#合并子序列
def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    #将剩下的列表内元素添加到后面
    result.extend(left)
    result.extend(right)
    return result

#递归拆分成子序列
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    #合并左右两边分组
    return merge(left,right)

#堆排序  大根堆用于升序，小根堆用于降序，最后一个非叶子节点下标为（n-2)//2  从上到下从0开始编号
# 左节点索引为2*i+1  右节点索引为2*i + 2

#创建大根堆
def heapify(arr,length,i):
    """
    :param arr:
    :param length: 整个数组序列的长
    :param i: 要堆化的根节点索引
    :return:
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < length and arr[left] > arr[largest]:
        largest = left
    if right < length and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        #继续向下对后面的子树构建大根堆
        heapify(arr,length,largest)

def heap_sort(arr):
    length = len(arr)
    #从最后一个非叶子节点从下往上构建大根堆
    for i in range((length-2)//2,-1,-1):
        heapify(arr,length,i)

    #对构建好的大根堆，将堆顶元素和堆尾元素进行交换，然后堆剩下的继续构建大根堆
    for i in range(length-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]  #arr[0]是堆顶元素，arr[i]是堆尾元素

        #对剩下的元素从堆顶开始更新
        heapify(arr,i,0)

    return arr

#计数排序 适用于一定范围内的整数排序，在取值范围不是很大的情况下，性能快过线性对数阶的排序算法
#不是基于元素比较，而是利用数组下标来确定元素的正确位置
#数组里右20个随机整数，取值范围是从0到10 ，从小到大排序
#按取值范围建立一个长度为11（10-0+1）的数组，数组下标为0-10，元素初始值全为0
#遍历这个随机数列，对每个数进行计数
#对所有的而技术累加（每一项等于当前项和前一项的和
#填充目标数组，将每个元素放在新数组的第C[i]项，每放一个元素，该元素的计数就减1

def count_sort(arr):
    length = len(arr)
    max_value = max(arr)
    #根据值的范围初始化计数列表
    count = [0 for _ in range(max_value+1)]
    #初始化输出的结果列表
    output = [0 for _ in range(length)]

    #对每个元素进行计数统计，元素从小到大作为索引
    for i in range(length):
        count[arr[i]] += 1

    #对计数进行累加
    for i in range(1,len(count)):
        count[i] += count[i-1]

    #对目标数组进行填充
    for i in range(length):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output




if __name__ == '__main__':
    arr = [39,9,79,17,19,15,16,2,82,89]
    # insert_sort(arr)
    # shell_sort(arr)
    # quick_sort(arr,0,len(arr)-1)
    # print(merge_sort(arr))
    # print(heap_sort(arr))
    # print(choose_sort(arr))



