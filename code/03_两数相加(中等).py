"""2021/03/04"""
"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""
""" NO.1 利用链表执行:
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val+l2.val)
        cur = head
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            cur.next = ListNode(l1.val + l2.val + cur.val//10)
            cur.val %= 10
            cur = cur.next
        if cur.val >=10:
            cur.next = ListNode(cur.val//10)
            cur.val %=10
        return head
"""
""" NO.2 利用递归执行:
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addTwo(a,b,integer):
            if not a and not b and not integer :return
            s = (a.val if a else 0)+(b.val if b else 0)+integer
            head = ListNode(s%10)
            head.next = addTwo(a.next if a else None,b.next if b else None,s//10)
            return head
        return addTwo(l1,l2,0)
"""