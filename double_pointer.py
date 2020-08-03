"""
双指针
"""
#2.判断一个字符串是否是另一个字符串的子序列，不要求连续
def sub_str(sub_str,old_str):
    m,n = len(sub_str),len(old_str)
    i,j = 0,0
    while (i < m) and (j < n):
        if sub_str[i] == old_str[j]:
            i += 1
        j += 1
    if i == m:
        return True
    else:
        return False

if __name__ == '__main__':
    substr = 'hel'
    string1 = 'yhoejl'
    print(sub_str(substr,string1))




