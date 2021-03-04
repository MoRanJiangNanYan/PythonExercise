"""2021/03/04"""
"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""


class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        s1 = ''
        s2 = ''
        for i in l1:
            s1 += str(i)
        for i in l2:
            s2 += str(i)
        return int(s1[::-1]) + int(s2[::-1])


l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(Solution.addTwoNumbers(l1, l2))
