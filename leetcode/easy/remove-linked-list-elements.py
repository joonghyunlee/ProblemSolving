# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        th = ListNode(0)
        th.next = head
        cp = th
        np = th.next
        while np:
            if np.val == val:
                cp.next = np.next
            else:
                cp = np
            np = np.next

        return th.next

    def toLinkedList(self, nums):
        h = ListNode(0)
        p = h
        for n in nums:
            p.next = ListNode(n)
            p = p.next
        h = h.next
        return h

    def printLinkedList(self, head):
        p = head
        while p:
            print p.val,
            p = p.next
        print


if __name__ == '__main__':
    s = Solution()
    head = s.toLinkedList([1,2,6,3,4,5,6])
    r = s.removeElements(head, 6)
    s.printLinkedList(r)
    head = s.toLinkedList([1,2,6,3,4,5,6])
    r = s.removeElements(head, 1)
    s.printLinkedList(r)
    head = s.toLinkedList([])
    r = s.removeElements(head, 6)
    s.printLinkedList(r)
    head = s.toLinkedList([1, 1, 1])
    r = s.removeElements(head, 1)
    s.printLinkedList(r)
