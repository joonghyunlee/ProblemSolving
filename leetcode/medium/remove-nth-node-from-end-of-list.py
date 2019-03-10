# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        q, qs = [], n + 1
        while p:
            q.insert(0, p)
            if len(q) > qs:
                q.pop()
            p = p.next
        if len(q) == qs:
            s = q.pop()
            t = q.pop()
            s.next = t.next
        else:
            t = q.pop()
            head = t.next
        return head

    def toList(self, nums):
        head, p = None, None
        for n in nums:
            if not p:
                p = ListNode(n)
            else:
                p.next = ListNode(n)
                p = p.next
            if not head:
                head = p
        return head

    def printList(self, head):
        p = head
        while p:
            print(p.val)
            p = p.next


if __name__ == '__main__':
    s = Solution()
    h = s.toList([1, 2, 3, 4, 5])
    r = s.removeNthFromEnd(h, 2)
    s.printList(r)
    h = s.toList([1])
    r = s.removeNthFromEnd(h, 1)
    s.printList(r)
    h = s.toList([1, 2])
    r = s.removeNthFromEnd(h, 2)
    s.printList(r)
