#!/user/bin/env python
#-*- coding:utf-8 -*-
# @Time    : 2018/12/20 13:56
# @Author  : 刘
# @Site    : 
# @File    : 873.py
# @Software: PyCharm

def lenLongestFibSubseq(A):
    """
    :type A: List[int]
    :rtype: int
    """
    G = set(A)
    ans = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            x, y = A[i], A[i] + A[j]
            length = 2
            while y in G:
                x, y = y, x + y
                length += 1
            ans = max(ans, length)
    return ans if ans >= 3 else 0


lenLongestFibSubseq(A=[2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50])