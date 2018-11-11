# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_candidate = l1
        r_candidate = l2

        head = None
        tail = None
        while l_candidate and r_candidate:
            if l_candidate.val <= r_candidate.val:
                if tail:
                    tail.next = l_candidate
                tail = l_candidate
                l_candidate = l_candidate.next
            elif l_candidate.val > r_candidate.val:
                if tail:
                    tail.next = r_candidate
                tail = r_candidate
                r_candidate = r_candidate.next

            if not head:
                head = tail

        if not l_candidate:
            if tail:
                tail.next = r_candidate
            else:
                head = r_candidate
        if not r_candidate:
            if tail:
                tail.next = l_candidate
            else:
                head = l_candidate

        return head

    def printList(self, l):
        head = l
        if not head:
            print head
            return

        print "%d" % head.val,
        head = head.next
        while head:
            print "->%d" % head.val,
            head = head.next
        print


if __name__ == '__main__':
    s = Solution()

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    r = s.mergeTwoLists(l1, l2)
    s.printList(r)

    l1 = None
    l2 = ListNode(0)
    r = s.mergeTwoLists(l1, l2)
    s.printList(r)
