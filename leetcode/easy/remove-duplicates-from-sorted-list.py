# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

    def printNodes(self, head):
        p = head
        if p:
            print('%d' % p.val),
            p = p.next
        while p:
            print('->%d' % p.val),
            p = p.next
        print


if __name__ == '__main__':
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(2)
    s.deleteDuplicates(a)
    s.printNodes(a)
    b = ListNode(1)
    b.next = ListNode(1)
    b.next.next = ListNode(2)
    b.next.next.next = ListNode(3)
    b.next.next.next.next = ListNode(3)
    s.deleteDuplicates(b)
    s.printNodes(b)
