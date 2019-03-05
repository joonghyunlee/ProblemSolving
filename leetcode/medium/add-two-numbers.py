# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry, p1, p2 = 0, l1, l2
        a = []
        while p1 or p2:
            ls = carry
            if p1: ls += p1.val
            if p2: ls += p2.val
            carry, ls = ls // 10, ls % 10
            a.append(ls)
            if p1: p1 = p1.next
            if p2: p2 = p2.next

        if carry:
            a.append(carry)

        h, p = None, ListNode(carry)
        for e in a:
            p.next = ListNode(e)
            p = p.next
            if not h: h = p
        return h

    def printList(self, li):
        p = li
        while p:
            print(p.val,)
            p = p.next
        print()


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    r = s.addTwoNumbers(l1, l2)
    s.printList(r)
