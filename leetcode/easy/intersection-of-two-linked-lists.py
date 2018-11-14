# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        while pA != pB:
            if not pA:
                pA = headB
            else:
                pA = pA.next

            if not pB:
                pB = headA
            else:
                pB = pB.next

        return pA


if __name__ == '__main__':
    s = Solution()
    headA = ListNode(4)
    headA.next = ListNode(5)
    headA.next.next = ListNode(6)
    headA.next.next.next = ListNode(7)
    headA.next.next.next.next = ListNode(8)
    headB = ListNode(1)
    headB.next = ListNode(2)
    headB.next.next = headA.next.next
    r = s.getIntersectionNode(headA, headB)
    print r.val if r else r
    headB.next.next = ListNode(3)
    r = s.getIntersectionNode(headA, headB)
    print r.val if r else r
    headA = ListNode(3)
    headB = ListNode(2)
    headB.next = headA
    r = s.getIntersectionNode(headA, headB)
    print r.val if r else r
