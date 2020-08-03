# -*- coding:utf-8 -*-
"""
动态规划相关
"""
"""
解决动态规划问题的三大步骤
1.创建一个保存历史数据的数组 dp[]或dp[][]
2.给出初始值
3.通过关系推导计算dp[n]

注意：一维数组和二维数组的初始化
一维数组： dp = [0] * m
二维数组： dp = [[0 for i in range(n+1)] for j in range(m+1)]  m行n列
"""
#level0  入门
#1.牛妹的蛋糕 每天吃掉当天的三分之一，到第n天吃的时候只剩下一个蛋糕，问刚开始吃的时候有多少个蛋糕
#dp[i] = dp[i-1] - (dp[i-1]//3 + 1)

import math
def cakeNumber(n):
    #每个元素表示当天的蛋糕数
    dp = [0] * n
    dp[n-1] = 1
    for i in range(n-2,-1,-1):
        dp[i] = 3 * (dp[i+1] + 1) // 2
    return dp[0]

#level1
#1.最小花费爬楼梯,每次可以爬1阶或2阶，每个阶梯都有对应的体力花费
def climb_stairs(cost):
    #初始化存放体力花费的数组,里面每个元素表示到达当前台阶所需要花费的最小体力值
    dp = [0] * len(cost)

    #初始化
    dp[0] = cost[0]
    dp[1] = cost[1]

    #递推公式
    for i in range(2,len(cost)):
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i]

    return dp[len(cost)-1]

#2.区域和检索  给定一个数组，求出数组从索引i到索引j范围内元素的和
#初始化dp 里面每个元素为以当前元素结尾的所有元素的和 i到j的可以用dp[j]-dp[i]
def sumRange(arr,i,j):
    #初始化存放数据的数组
    length = len(arr)
    dp = [0] * length
    dp[0] = arr[0]
    for i in range(1,length):
        dp[i] = dp[i-1] + arr[i]

    return dp[j] - dp[i]

#打家劫舍 每个房子存在一定的金额，但是不能偷连续两间,
def rob(nums):
    #初始化存放历史数据的数组，每个元素表示以当前元素结尾的最大金额,要么是前以节点的累计最大金额，要么是前两个节点的累计最大金额加该节点的值
    length = len(nums)
    dp = [0] * length
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(1,length):
        dp[i] = max(dp[i-1],dp[i-2] + nums[i])
    return dp[-1]

#买股票的最佳时期 不能在买入前卖出，每天只能买入或卖出一种
def maxProfit(nums):
    length = len(nums)
    #初始化存放数据的数组，dp[i]表示第i天的最大利润
    dp = [0] * length
    #初始化最小值
    minprice = nums[0]

    for i in range(length):
        minprice = min(minprice,nums[i])
        dp[i] = max(dp[i-1],nums[i] - minprice)

    return dp[-1]

#爬楼梯，每次可以爬一阶或者两阶
def climb_stair2(n):
    #里面元素表示i阶台阶的方法数
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

#最大和的连续子序列
def maxSubArray(nums):
    #初始化数组，里面每个元素表示当前位置结尾的最大子序列和
    length = len(nums)
    dp = [0] * length
    dp[0] = nums[0]
    for i in range(1,length):
        dp[i] = max(dp[i-1] + nums[i],nums[i])

    return max(dp)

#二维矩阵上从左上角走到右下角可以拿到的最大价值，每次只能向下或向右移动
def getMost(board):
    #初始化二维数组
    dp = [[0] for i in range(6) for j in range(6)]
    #当只有一行或一列的时候，只能想一个方向移动
    for i in range(6):
        dp[i][0] = dp[i-1][0] + board[i][0]

    for j in range(6):
        dp[0][j] = dp[0][j-1] + board[0][j]

    for i in range(1,6):
        for j in range(1,7):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + board[i][j]

    return dp[5][5]

#二维矩阵，机器人从左上角走到右下角，每次只能向下或向右，求路径总数
def move(m,n):
    dp = [[0] for i in range(n) for j in range(m)]
    #初始值，当只有一列或一行时，只有一条路径
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

#编辑距离 一个单词转换为另一个单词的最少操作步数，可以插入，删除，替换
#dp[i][j] 表示单词i转换为单词j的最少操作步数
#如果str1[i] == str2[j]  则最少步数为dp[i-1][j-1]
#如果不相等
    #如果str1[i] 替换成str2[j]相等 则操作步数为dp[i-1][j-1] + 1
    #如果str1[i] 删除之后相等，则操作步数为dp[i-1][j] + 1
    #如果增加后相等，则为dp[i][j-1] + 1
def editDistance(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0] for i in range(len1) for j in range(len2)]

    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1

    return dp[len1-1][len2-1]

"""
背包问题：给定n种物品和一个容量为C的背包，物品i的重量为Wi,其价值为vi
如何选择背包的价值最大，每个物品可以选择装与不装
声明二维数组dp[i][j] 表示面对第i个物品时，背包容量为j时所获得的最大价值
对每个物品进行考虑
如果物品wi > C dp[i][j] = dp[i-1][j]
如果物品wi < C,分该物品拿与不拿
拿 dp[i][j] = dp[i-1][j-wi] + vi
不拿 dp[i-1][j]  
"""
def bag(w,v,n,c):
    #c表示的背包的容量 n表示物品的种类  物品的种类作为行，容量范围作为列构建矩阵
    dp = [[0] for i in range(c+1) for j in range(n)]

    #初始化，当物品种类为0的时候，没有东西可以拿
    for i in range(c+1):
        dp[0][i] = 0

    #当背包的容量为o的时候，没有办法装东西
    for j in range(n):
        dp[j][0] = 0

    for i in range(1,n):
        for j in range(1,c+1):
            dp[i][j] = max(dp[i-1][j-w[i]] + v[i],dp[i-1][j])

    return dp[n-1][c-1]

#乘积最大的连续子序列






#level2 中等
#最长公共子序列 两个字符串的最长公共子序列的长度，不要求连续
def logestCommonSubsequence(str1,str2):
    m = len(str1)
    n = len(str2)
    #初始化存放历史数据的数组  m+1行n+1列
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 0

    for j in range(n+1):
        dp[0][j] = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]










if __name__ == '__main__':
    # cost = [1,100,1,1,1,100,1,1,100,1]
    # print(climb_stairs(cost))
    # nums = [-2,0,3,-5,2,-1]
    # print(sumRange(nums,2,0))
    # nums = [2,7,9,3,1]
    # print(rob(nums))
    # nums = [7,1,5,3,6,4]
    # nums = [7,6,5,4,3]
    # print(maxProfit(nums))
    # print(climb_stair2(3))

    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # print(maxSubArray(nums))
    # text1 = "abcde"
    # text2 = "ace"
    # print(logestCommonSubsequence(text1,text2))
    print(cakeNumber(2))


