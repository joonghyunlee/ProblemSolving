# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        queue = []

        dh = ListNode(None)
        dh.next = head

        i, p = 0, dh
        while p:
            if i == m - 1:
                oh = p
                p = p.next
            elif i == m:
                nt = np = p
                p = p.next
            elif i > m and i < n:
                np, p.next, p = p, np, p.next
            elif i == n:
                nt.next, p.next = p.next, np
                oh.next = p
                break
            else:
                p = p.next
            i += 1
        return dh.next

    def toList(self, nums):
        p = head = ListNode(None)
        for n in nums:
            p.next = ListNode(n)
            p = p.next
        return head.next

    def printList(self, head):
        p = head
        while p:
            print p,
            p = p.next
        print()


if __name__ == '__main__':
    s = Solution()
    head = s.toList([1, 2, 3, 4, 5])
    s.printList(head)
    r = s.reverseBetween(head, 2, 4)
    s.printList(r)
    head = s.toList([1, 2, 3])
    s.printList(head)
    r = s.reverseBetween(head, 1, 3)
    s.printList(r)
