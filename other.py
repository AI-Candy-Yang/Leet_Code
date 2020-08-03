

#几张卡牌，每次可以从开头或末尾抽取一张，求拿到k张的最大点数
#每次只能从左或从右进行抽取，计算得到的最大值，逆向思维就是求中间长度为length-k的连续子序列和的最小值
#采用滑动窗口的方式实现，求固定长度的连续子序列的和的最小值
def max_score(cardPoints,k):
    if len(cardPoints) == k:
        return sum(cardPoints)
    #初始化滑动窗口的最小值
    min_sum = sum(cardPoints[:len(cardPoints)-k])
    current_sum = min_sum
    right_index,left_index = len(cardPoints)-k-1,0
    for _ in range(k): #滑动K次
        left_index += 1
        right_index += 1
        #重新计算窗口内的值 减去之前左边界的值，加上现在新增的右边界的值
        current_sum = current_sum - cardPoints[left_index-1] + cardPoints[right_index]
        min_sum = min(current_sum,min_sum)
    return sum(cardPoints) - min_sum

