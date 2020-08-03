"""
递归
"""
"""
递归三要素：
1.定义函数，并定义它的功能
2.寻找递归结束条件
3.找出函数的递推关系式
"""
#两个字符串求和
def add_string(str1,str2):
    res = ""
    i,j,carry = len(str1)-1,len(str2)-1,0
    while (i >= 0) or (j >= 0):
        num1 = int(str1[i]) if i >= 0 else 0
        num2 = int(str2[j]) if j >= 0 else 0
        #初始化三个变量，分别表示当前位的数字相加之后的结果，进位数，余数
        tmp = num1 + num2 + carry
        carry = tmp // 10
        res = str(tmp % 10) + res
        i,j = i-1,j-1
    return "1" + res if carry else res

#第N个泰波那契数
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    #用三个变量来保存，空间复杂度只有O(1)
    x,y,z = 0,1,1
    for _ in range(n-2):  #不断的更新这三个变量
        x,y,z = y,z,x+y+z
    return z


