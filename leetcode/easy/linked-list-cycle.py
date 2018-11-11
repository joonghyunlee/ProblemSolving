# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        while p:
            n = p.next
            if n == head:
                return True
            p.next = head
            p = n
        return False


if __name__ == '__main__':
    s = Solution()

    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = head
    r = s.hasCycle(head)
    print r

    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    r = s.hasCycle(head)
    print r
